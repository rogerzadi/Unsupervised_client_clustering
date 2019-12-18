import pandas as pd
class clusterization:

    def __init__(self, data):
        self.data = data
        self.groupdum(data)

    def groupdum(self, data):
        data['DateTime'] = pd.to_datetime(data['DateTime'], format='%Y-%m-%d %H:%M:%S')
        dummies = pd.get_dummies(data.category, drop_first=False)
        piped = pd.concat([data, dummies], axis=1)
        self.group(piped)

    def group(self, piped):
        self.piped_group = piped.groupby(['DateTime', 'Transaction']).sum()
        self.piped_group.reset_index(level='DateTime', inplace=True)
        self.piped_group['day'] = self.piped_group.DateTime.dt.day_name()
        self.piped_group['hour'] = self.piped_group.DateTime.dt.hour
        piped_dummy = pd.get_dummies(data=self.piped_group, columns=['day']).drop('DateTime', axis=1)
        self.pca(piped_dummy)

    def pca(self, piped_dummy):
        from sklearn.decomposition import PCA
        pca = PCA(n_components=4).fit_transform(piped_dummy)
        pc_df = pd.DataFrame(pca, columns=[f'pc_{i + 1}' for i in range(4)])
        self.pc_df = pc_df
        self.cluster(pc_df)

    def cluster(self, pc_df):
        from sklearn.cluster import KMeans
        kmeans = KMeans(n_clusters=4).fit(pc_df)
        self.outputgroup(kmeans, pc_df)

    def outputgroup(self, kmeans, pc_df):
        import seaborn as sns
        cm = sns.light_palette('green', as_cmap=True)
        self.piped_group['label'] = kmeans.predict(pc_df)
        piped_merge = pipe.merge(self.piped_group.reset_index()[['label', 'Transaction']], on='Transaction', how='left')
        print(pd.crosstab(self.piped_group.hour, self.piped_group.label).style.background_gradient(cmap=cm))
        print(pd.crosstab(self.piped_group.day, self.piped_group.label).style.background_gradient(cmap=cm))
        self.outputbest(piped_merge)

    def outputbest(self, piped_merge):
        print(piped_merge.groupby('label')['Item'].value_counts().to_frame('counts').reset_index().set_index(
            'Item').groupby('label')['counts'].nlargest(10))

pipe=pd.read_csv("muestra6dias.csv")
clusterization(pipe)