
keyword_list = """False            class          from         or    
None              contunue         global         pass 
True              def              if             raise 
and               del              import         return
as                elif             in             try
assert            else             is             while
async             except           lambda         with
await             finally          nonlocal       yield
break             for              not""".split()
keyword_list_amount = len(keyword_list)
data = {"False": True, "assert": None}

for keyword in keyword_list:
    answer = input(f"проходили/не проходили: ({keyword})? ")
    if answer:
        data[keyword] = True
    else:
        data[keyword] = None

for key, value in data.items():
    print(f"{key}: {value}")

