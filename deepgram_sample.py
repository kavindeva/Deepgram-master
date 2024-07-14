import http.client

conn = http.client.HTTPSConnection("brain.deepgram.com")

payload = "{\"url\":\"string\"}"

headers = {
    'content-type': "application/json",
    'Authorization': "Basic a2F2aW5AbGFuaW5ub3ZhdGlvbnMuY29tOmthdmluXzI0MTk5Ng=="
    }

conn.request("POST", "/v2/listen", payload, headers)

res = conn.getresponse()
data = res.read()

print("hello kavin")
print(data.decode("utf-8"))
