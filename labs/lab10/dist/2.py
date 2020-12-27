import datetime

class Monitor:
    def __init__(self, firm_name, date_of_made, date_of_purchase, price, type, size):
        self.firm_name = firm_name
        self.date_of_made = datetime.date(*list(map(int, date_of_made.split("."))))
        self.date_of_purchase = datetime.date(*list(map(int, date_of_purchase.split("."))))
        self.price = price
        self.type = type
        self.size = size

    def get_age(self):
        return datetime.date.today() - self.date_of_made

    def is_display_the_image(self, img_size):
        return img_size[0] < self.size[0] and img_size[1] < self.size[1]

    def get_img_scale(self, img_size):
        x_scale = 1
        y_scale = 1
        scale_without_bad_quality = 1
        if img_size[0] > self.size[0]:
            x_scale = self.size[0]/img_size[0]

        if img_size[1] > self.size[1]:
            y_scale = self.size[1]/img_size[1]

        if x_scale < y_scale:
            scale_without_bad_quality = x_scale
        elif x_scale > y_scale:
            scale_without_bad_quality = y_scale

        return [[x_scale, y_scale], scale_without_bad_quality]

test1 = Monitor(1, "2017.5.17", "2014.11.18", 1, 2, [1028, 960])

print(test1.get_img_scale([2256, 1261]))