# Take inches and display cm and mm

inches = float(input("Enter inches :"))
cm = inches * 2.4
mm = cm * 10

print(f"Inches {inches} = {cm:6.2f} cm, {mm:6.2f} mm")
