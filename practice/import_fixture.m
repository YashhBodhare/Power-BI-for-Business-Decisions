// Create pFixturePath as a Text parameter containing the absolute local JSON path.
// Query name: PayBridgeRaw. Disable load for this staging query.
let
    Source = Json.Document(File.Contents(pFixturePath))
in
    Source

// Create a SEPARATE query named FactAttempt with the following expression.
let
    Source = Table.FromRecords(PayBridgeRaw[FactAttempt]),
    Typed = Table.TransformColumnTypes(Source, {
        {"AttemptID", type text}, {"PaymentID", type text},
        {"MerchantKey", Int64.Type}, {"CountryKey", Int64.Type}, {"ChannelKey", Int64.Type},
        {"AttemptDate", type date}, {"Status", type text},
        {"AmountINR", Currency.Type}, {"FeeRate", type number}
    }, "en-US")
in
    Typed

// Create a SEPARATE query named FactSettlement with the following expression.
let
    Source = Table.FromRecords(PayBridgeRaw[FactSettlement]),
    Typed = Table.TransformColumnTypes(Source, {
        {"SettlementID", type text}, {"PaymentID", type text},
        {"MerchantKey", Int64.Type}, {"CountryKey", Int64.Type}, {"ChannelKey", Int64.Type},
        {"SuccessfulAttemptDate", type date}, {"DueDate", type date}, {"SettlementDate", type date},
        {"AmountINR", Currency.Type}
    }, "en-US")
in
    Typed

// For EACH dimension/entitlement query, use the appropriate record field, e.g.:
// Table.FromRecords(PayBridgeRaw[DimMerchant])
// Table.FromRecords(PayBridgeRaw[DimCountry])
// Table.FromRecords(PayBridgeRaw[DimChannel])
// Table.FromRecords(PayBridgeRaw[UserCountryAccess])
// Set each key column to Whole Number; all descriptive fields and UPN to Text.
// This file contains separate snippets, not one executable combined M query.
