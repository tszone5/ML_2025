print("Grocery Bill Calculator")
print("-----------------------")

total = 0

while True:
    price = input("Enter item price (or 'done' to finish): ")
    if price == 'done':
        break
    
    quantity = input("Enter quantity: ")
    
    total += float(price) * int(quantity)

gst = total * 0.18
final_total = total + gst

print("\nBill Details:")
print(f"Subtotal: ₹{total:.2f}")
print(f"GST (18%): ₹{gst:.2f}")
print(f"Total: ₹{final_total:.2f}")
