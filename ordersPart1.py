import csv

#FILENAME = "orders.csv"
FILENAME = "C:/Users/Nik/Desktop/orders.csv"

# orders = [
#     ['1','17','15','10','1'], # N заказа; кол-во колбасы; кол-во салата; кол-во сыра; здесь - 1 / с собой - 0
#     ['2','1','3','5','0'],
#     ['3','2','12','8','1'],
#     ['4','7','15','4','0'],
#     ['5','18','13','6','0'],
#     ]
priceList = {"base": 100, "sausage": 10, "salad": 5, "cheese": 7, "extra": 15}
ordersParams = []
orderSum = []

# def WriteOrders():
#     with open(FILENAME, "w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerows(orders)

def ReadOrders():
    with open(FILENAME, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            ordersParams.append(row)