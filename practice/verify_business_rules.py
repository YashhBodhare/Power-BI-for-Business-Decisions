"""Independent arithmetic checks for the fictional fixture; does not execute DAX or M."""
from pathlib import Path
from decimal import Decimal
from datetime import date
import json

def main():
    data=json.loads(Path(__file__).with_name('paybridge.json').read_text())
    all_attempts=data['FactAttempt'];all_settlements=data['FactSettlement']
    assert len({r['AttemptID'] for r in all_attempts})==len(all_attempts)
    assert len({r['PaymentID'] for r in all_settlements})==len(all_settlements)
    for dim,key in [('DimMerchant','MerchantKey'),('DimCountry','CountryKey'),('DimChannel','ChannelKey')]:
        keys={r[key] for r in data[dim]};assert len(keys)==len(data[dim])
        assert all(r[key] in keys for r in all_attempts+all_settlements)
    print('PASS: grains, reference uniqueness and referential coverage')
    attempts=[r for r in all_attempts if '2026-01-01'<=r['AttemptDate']<'2026-03-01']
    success=[r for r in attempts if r['Status']=='Succeeded'];failed=[r for r in attempts if r['Status']=='Failed']
    assert len(attempts)==10 and len(success)==6 and len(failed)==4
    assert Decimal(len(success))/len(attempts)==Decimal('0.6')
    assert Decimal(len(failed))/len(attempts)==Decimal('0.4')
    print('PASS: Jan-Feb 2026 attempts 10; success 60%; failure 40%')
    distinct_payments={r['PaymentID'] for r in attempts}
    assert len(distinct_payments)==8 and len({r['PaymentID'] for r in success})==6
    assert Decimal(6)/8==Decimal('0.75')
    print('PASS: payment-based success 75%; distinct from attempt-based 60%')
    amount=sum(r['AmountINR'] for r in success)
    fees=sum(Decimal(r['AmountINR'])*Decimal(r['FeeRate']) for r in success)
    assert amount==4100 and fees==56
    print('PASS: successful amount INR 4100; fee revenue INR 56')
    monthly={m:sum(r['AmountINR'] for r in success if r['AttemptDate'].startswith(m)) for m in ['2026-01','2026-02']}
    assert monthly=={'2026-01':3000,'2026-02':1100}
    prior=sum(r['AmountINR'] for r in all_attempts if r['Status']=='Succeeded' and '2025-01-01'<=r['AttemptDate']<'2025-03-01')
    assert prior==900 and sum(monthly.values())==amount
    print('PASS: Jan 3000, Feb 1100; prior-year corresponding amount 900')
    settlements=[r for r in all_settlements if '2026-01-01'<=r['SettlementDate']<'2026-03-01']
    late=[r for r in settlements if r['SettlementDate']>r['DueDate']]
    days=sum((date.fromisoformat(r['SettlementDate'])-date.fromisoformat(r['SuccessfulAttemptDate'])).days for r in settlements)
    assert len(settlements)==6 and len(late)==3 and sum(r['AmountINR'] for r in late)==2800 and days==10
    print('PASS: 6 settlements; 3 late; late amount 2800; mean elapsed days 10/6')
    countries={r['CountryKey']:r['Country'] for r in data['DimCountry']}
    shares={name:Decimal(sum(r['AmountINR'] for r in success if r['CountryKey']==key))/amount for key,name in countries.items()}
    assert abs(sum(shares.values())-1)<Decimal('0.000000000000000000000000001')
    assert sum(r['AmountINR'] for r in success if r['CountryKey']==1)==1600
    print('PASS: country amount contributions reconcile to 100%')
    allowed={r['CountryKey'] for r in data['UserCountryAccess'] if r['UPN']=='regional-ops@example.invalid'}
    visible=[r for r in attempts if r['CountryKey'] in allowed]
    assert allowed=={1,4} and len(visible)==7
    assert not {r['CountryKey'] for r in data['UserCountryAccess'] if r['UPN']=='unknown@example.invalid'}
    print('PASS: entitlement expectations India + Singapore = 7 attempts; unmapped has none')
    print('All 8 independent checks passed. Confirm engine behaviour in Power BI separately.')

if __name__=='__main__':main()
