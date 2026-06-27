with open('gamemodes/SALRP.pwn', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Fix forward
content = content.replace(
    'forward car_Reset(carid,save,bool:recreate=true,bool:sqlidd=false)',
    'forward car_Reset(carid,save,bool:recreate,bool:sqlidd)'
)
# Fix public
content = content.replace(
    'public car_Reset(carid,save,bool:recreate=true,bool:sqlidd=false)',
    'public car_Reset(carid,save,bool:recreate,bool:sqlidd)'
)

with open('gamemodes/SALRP.pwn', 'w', encoding='utf-8', errors='replace') as f:
    f.write(content)

print("Done")
