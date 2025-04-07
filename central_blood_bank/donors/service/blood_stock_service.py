

from datetime import date, timedelta
from central_blood_bank.donors.models import BloodStock



class BloodStockService:
    model  = BloodStock


    def create_blood_stock(self, donor):
        blood_stock = self.model(
            blood_type=donor.blood_type,
            city=donor.city,
            donor=donor
        )
        blood_stock.save()
        return blood_stock