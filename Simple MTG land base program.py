print("This is my first custom program.")

print("I will tell you how many basics to run of each type.")
print("How many White symbols are in your deck?")
whites = int(input())
print("How many Blue symbols are in your deck?")
blues = int(input())
print("How many Red symbols are in your deck?")
reds = int(input())
print("How many Black symbols are in your deck?")
blacks = int(input())
print("How many Green symbols are in your deck?")
greens = int(input())
print("How many basic lands are you running?")
basics = int(input())
total = whites + blues + reds + blacks + greens

plainsnum = (whites / total) * basics
islandsnum = (blues / total) * basics
swampsnum = (blacks / total) * basics
mountainsnum = (reds / total) * basics
forestsnum = (greens / total) * basics

print(f"Since you are running {basics} basic lands, you will need:")
print(f"Plains: {plainsnum}")
print(f"Islands: {islandsnum}")
print(f"Swamps: {swampsnum}")
print(f"Mountains: {mountainsnum}")
print(f"Forests: {forestsnum}")

input()
