

class Utility:
    @staticmethod
    def complement_year(year):
        year_replaced = int(year.replace("　", "").replace(" ", ""))
        if str(year_replaced).startswith("9"):
            return 1900 + year_replaced
        elif (str(year_replaced).startswith("0"))|(str(year_replaced).startswith("1")):
            return 2000 + year_replaced