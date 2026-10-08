"""Create small fictional PayBridge learning data; no real payment or customer data."""
from pathlib import Path
import json

def create():
    merchants = [
        dict(MerchantKey=1,Merchant='Merchant One',City='Mumbai',RiskTier='Standard'),
        dict(MerchantKey=2,Merchant='Merchant Two',City='Thane',RiskTier='Standard'),
        dict(MerchantKey=3,Merchant='Merchant Three',City='Dubai',RiskTier='Review'),
        dict(MerchantKey=4,Merchant='Merchant Four',City='London',RiskTier='Standard'),
        dict(MerchantKey=5,Merchant='Merchant Five',City='Singapore',RiskTier='Review'),
        dict(MerchantKey=6,Merchant='Merchant Six',City='New York',RiskTier='Standard'),
    ]
    for merchant, country_key in zip(merchants, [1, 1, 2, 3, 4, 5]):
        merchant['CountryKey'] = country_key
    countries=[dict(CountryKey=i,Country=c) for i,c in enumerate(['India','UAE','UK','Singapore','US'],1)]
    channels=[dict(ChannelKey=1,Channel='UPI'),dict(ChannelKey=2,Channel='Card')]
    # AmountINR is already an approved reporting-currency value in this teaching fixture.
    data=[
      ('A01','P01',1,1,1,'2026-01-05','Failed',1000,'0.01'),
      ('A02','P01',1,1,1,'2026-01-05','Succeeded',1000,'0.01'),
      ('A03','P02',2,1,2,'2026-01-10','Succeeded',500,'0.01'),
      ('A04','P03',3,2,2,'2026-01-15','Failed',800,'0.01'),
      ('A05','P04',4,3,2,'2026-01-20','Succeeded',1500,'0.02'),
      ('A06','P05',5,4,1,'2026-02-02','Failed',700,'0.01'),
      ('A07','P05',5,4,1,'2026-02-03','Succeeded',700,'0.01'),
      ('A08','P06',6,5,2,'2026-02-05','Succeeded',300,'0.01'),
      ('A09','P07',1,1,1,'2026-02-06','Failed',400,'0.01'),
      ('A10','P08',2,1,2,'2026-02-10','Succeeded',100,'0.01'),
      ('A25-01','P25-01',1,1,1,'2025-01-05','Succeeded',600,'0.01'),
      ('A25-02','P25-02',2,1,2,'2025-02-10','Succeeded',300,'0.01'),
    ]
    fields=['AttemptID','PaymentID','MerchantKey','CountryKey','ChannelKey','AttemptDate','Status','AmountINR','FeeRate']
    attempts=[dict(zip(fields,row)) for row in data]
    dates={
      'P01':('2026-01-06','2026-01-07'), 'P02':('2026-01-11','2026-01-11'),
      'P04':('2026-01-21','2026-01-23'), 'P05':('2026-02-04','2026-02-04'),
      'P06':('2026-02-06','2026-02-08'), 'P08':('2026-02-11','2026-02-10'),
      'P25-01':('2025-01-06','2025-01-06'), 'P25-02':('2025-02-11','2025-02-11')}
    settlements=[]
    for a in attempts:
        if a['Status']=='Succeeded':
            due,actual=dates[a['PaymentID']]
            settlements.append(dict(SettlementID='S-'+a['PaymentID'],PaymentID=a['PaymentID'],
                MerchantKey=a['MerchantKey'],CountryKey=a['CountryKey'],ChannelKey=a['ChannelKey'],
                SuccessfulAttemptDate=a['AttemptDate'],DueDate=due,SettlementDate=actual,AmountINR=a['AmountINR']))
    access=[dict(UPN='india-ops@example.invalid',CountryKey=1),
            dict(UPN='regional-ops@example.invalid',CountryKey=1),dict(UPN='regional-ops@example.invalid',CountryKey=4)]
    fixture=dict(DimMerchant=merchants,DimCountry=countries,DimChannel=channels,
                 FactAttempt=attempts,FactSettlement=settlements,UserCountryAccess=access)
    path=Path(__file__).with_name('paybridge.json')
    path.write_text(json.dumps(fixture,indent=2),encoding='utf-8')
    return path

if __name__=='__main__':
    print(create())
