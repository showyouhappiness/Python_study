class Scale:
    def check(self):
        if self.count_person > 500:
            return "%s是个大公司." % self.name
        else:
            return "%s是个小公司." % self.name


class Detail:
    def show(self, scale):
        print("%s,公司有%s名员工." % (scale, self.count_person))


class Company(Scale, Detail):
    def __init__(self, name, count):
        self.name = name
        self.count_person = count


if __name__ == "__main__":
    my_company = Company("JK", 600)
    company_scale = my_company.check()
    my_company.show(company_scale)
