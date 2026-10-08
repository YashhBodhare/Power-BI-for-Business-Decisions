# 🧪 PayBridge learning fixture and validation

[← Study hub](../README.md) · [Case schema](../CASE_STUDY.md) · [DAX measures](measures.dax)

This companion contains fictional JSON data and independently checked expected results. It does not contain a PBIX file. DAX and M have been reviewed but not executed in a Power BI engine in this environment.

## Independent result checks

With Python 3 available, run from the repository root:

```bash
python3 practice/verify_business_rules.py
```

No third-party packages or network calls are required. All eight checks passed against the included fixture: grains and references, attempt rates, logical-payment rates, amounts/fees, monthly/prior-year amounts, settlements, country contribution and entitlement expectations.

`create_fixture.py` can regenerate the same fictional `paybridge.json`. It is not a loader for real customer or payment data.

## Build the learning model in Desktop

1. Use the local `paybridge.json` file. Create a Text parameter named `pFixturePath` containing its full local path.
2. Follow [import_fixture.m](import_fixture.m): create PayBridgeRaw as a staging query with load disabled, then separate FactAttempt, FactSettlement, dimension and entitlement queries. The file contains several separate snippets, not one combined executable M query.
3. Set identifiers and descriptions to Text, dimension keys to Whole Number, date fields to Date, AmountINR to Fixed decimal number and FeeRate to Decimal number.
4. Create DimDate using the calculated-table example in [question 021](../chapters/02-data-modelling.md#pbi-021). Mark Date as the date-table column and sort YearMonth by YearMonthSort.
5. Create the [documented relationships](../CASE_STUDY.md#base-relationships). Keep both facts separate and UserCountryAccess disconnected.
6. Add each definition in `measures.dax` as a separate measure. Apply currency and percentage formats. The file is a collection of measure definitions, not one DAX query to paste into a query window.
7. Build cards for attempts, success/failure rate, successful amount and late settlements. Add a country table, a channel comparison and a month trend.
8. Set the baseline date selection to **January–February 2026**. The full fixture has extra 2025 data, so an unfiltered all-time card will not show the baseline totals.

## Expected baseline

| Measure | Expected January–February 2026 result |
|---|---:|
| Attempt Count | 10 |
| Successful Attempts / Failed Attempts | 6 / 4 |
| Success Rate / Failure Rate | 60% / 40% |
| Logical Payment Count | 8 |
| Logical Payment Success Rate | 75% |
| Successful Amount INR / Fee Revenue INR | 4,100 / 56 |
| Settlement Count / Late Settlements | 6 / 3 |
| Late Settlement Rate | 50% |
| Settled Amount INR | 4,100 |
| Late Settled Amount INR | 2,800 |
| Mean Settlement Days | 1.666… |

January successful amount is 3,000; February is 1,100. Corresponding January–February 2025 successful amount is 900. The fixture has no April rows; the fixed April measure should be blank before any deliberate zero presentation policy.

## Desktop checks to complete

- Compare all baseline cards with the table above, then check each country and channel.
- Verify total success rate is 60%; the unweighted average of the five country rates is 62%, which is not the company rate.
- Confirm retries P01 and P05 increase attempts without doubling successful payment value.
- Check a contradictory status selection and define whether rate visuals should ignore that slicer's interaction.
- Test country share-of-all versus share-of-selected with a restricted selection; keep both denominators labelled.
- Test actual SettlementDate versus DueDate. A payment can fall into different periods under those roles.
- Check the selected-date end point for YTD and prior-year comparisons.
- Test blank groups and missing-period presentation; do not infer a complete production history from this tiny fixture.

## Service and security checks to complete

1. Create one role with the DimCountry entitlement expression in [question 041](../chapters/04-service-and-connectivity.md#pbi-041). Apply the equivalent DimMerchant[CountryKey] rule to DimMerchant, and the separate UPN identity rule to UserCountryAccess, as described in the [security scope](../CASE_STUDY.md#security-rule-scope).
2. Replace fictional `.invalid` identities with authorised test identities when doing an actual service exercise. The fixture's addresses are intentionally not real login accounts.
3. Assign the role and test through **consumer/Viewer** access. Editing workspace roles do not demonstrate RLS enforcement.
4. For the regional identity's India + Singapore entitlement, expect **7 attempts, 4 successes and INR 2,300 successful amount** in the baseline.
5. Confirm an unmapped identity receives no country entitlement, and that exports, drillthrough and global benchmarks remain restricted as intended.
6. Validate service connections, credentials, gateway requirements, refresh history and freshness presentation in the actual environment.
7. Check approved application distribution and the required licensing/capacity before sharing.

A local file-path fixture is a Desktop learning source. Service refresh needs an appropriate supported connection arrangement; it does not gain access to your local path just because the report was published.

Record these engine/service checks as completed only after performing them. Independent Python arithmetic cannot prove actual DAX evaluation, M behaviour, relationship propagation or RLS enforcement.
