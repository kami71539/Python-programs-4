monthconversion={
"Jan":"January",
"Feb":"February",
"Mar":"March",
"Apr":"April",
"May":"May",
6:"June",
"Jul":"July",
"Aug":"August",
"Sep":"September",
"Oct":"October",
"Nov":"November",
"Dec":"December"
}
print(monthconversion.get("Mar"))
print(monthconversion["Jul"])
print(monthconversion[6])
print(monthconversion.get("A value not found in the dict"))
print(monthconversion.get("A value not found in the dict","Not a valid month."))
