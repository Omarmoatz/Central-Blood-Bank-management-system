# from datetime import date

# from central_blood_bank.donors.models import BloodStock


# class BloodStockService:
#     model = BloodStock

#     def __init__(self, donor):
#         self.donor = donor

#     def create_blood_stock(self):
#         blood_stock = self.model(
#             blood_type=self.donor.blood_type,
#             city=self.donor.city,
#             donor=self.donor,
#         )
#         blood_stock.save()

#         self.donor.last_donation = date.today()
#         self.donor.save()
#         return blood_stock
