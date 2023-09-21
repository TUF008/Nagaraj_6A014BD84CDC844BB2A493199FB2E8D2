def linearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices


# Example usage:
products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target1 = "shoes"
result1 = linearSearchProduct(products, target1)
print(result1)
target2 = "apple"
result2 = linearSearchProduct(products, target2)
print(result2)