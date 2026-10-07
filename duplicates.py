student_data={
"id1":{"name":"tanmay","class":8,"subject":"english,maths,science"},
"id2":{"name":"bliss","class":8,"subject":"english,maths,science"},
"id3":{"name":"mike","class":8,"subject":"english,maths,science"},
"id4":{"name":"tanmay","class":8,"subject":"english,maths,science"}
}
result={}
seen_keys=[]

for i,j in student_data.items():
    unique_key=(j["name"],j["class"],j["class"])
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[i]=j

for k,v in result.items():
    print(k, " : ",v)