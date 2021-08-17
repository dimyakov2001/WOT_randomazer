from scipy.stats import norm


class NormalLevelDistribution:

    @staticmethod
    def generate_rvs(mean, std, size=1):
        return norm.rvs(loc=mean, scale=std, size=size)

    @staticmethod
    def generate_pdf(axis, mean, std):
        return norm.pdf(axis, mean, std)
