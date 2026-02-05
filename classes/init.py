class movie:
    def __init__(self,title,rating):
        self.title=title
        self.rating=rating
    def review(self):
        print(f"Movie title is {self.title} and Rating is: {self.rating}")
movie1=movie("KGF","5 star")
movie2=movie("RRR","4.5 star")
movie1.review()
movie2.review()
