class India:
    def capital(self):
        print("capital of India is Delhi")

    def language(self):
        print("Hindi is most spoken language in India")

    def type(self):
        print("it is a developing country")

class USA:
    def capital(self):
        print("capital of USA is washington")

    def language(self):
        print("english is most spoken language in India")

    def type(self):
        print("it is a developed country")

I=India()
U=USA()

for country in (I,U):
    country.capital()
    country.language()
    country.type()