import json
import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pdb


chrome_driver_path = "C:\\Users\\lch_a\\OneDrive\\Documentos\\GitHub\\code_challenge_v1\\chromedriver.exe"  
chrome_options = Options()
chrome_options.add_argument('--headless') 

driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

json_url = "https://storage.googleapis.com/resources-prod-shelftia/scrapers-prueba/product.json"

driver.get(json_url)
time.sleep(2)  

# Obtener el contenido JSON de la página
json_text = driver.find_element_by_tag_name("body").text
data = json.loads(json_text)
all_variants = data['allVariants'][0] 
attributes_raw = all_variants['attributesRaw']


custom_attributes = next(attr for attr in attributes_raw if attr['name'] == 'custom_attributes')
value_attributes_string = custom_attributes['value']['es-CR']

#Parsear el JSON dentro de value_attributes_string
value_attributes = json.loads(value_attributes_string)

#alergias 
allergens_data = value_attributes.get("allergens", {})
allergens = [allergen['name'] for allergen in allergens_data.get('value', [])]

#extrae los otros datos 
sku = value_attributes.get("sku", {}).get('value', "")
vegan = value_attributes.get("vegan", {}).get('value', False)
kosher = value_attributes.get("kosher", {}).get('value', False)
organic = value_attributes.get("organic", {}).get('value', False)
vegetarian = value_attributes.get("vegetarian", {}).get('value', False)
gluten_free = value_attributes.get("gluten_free", {}).get('value', False)
lactose_free = value_attributes.get("lactose_free", {}).get('value', False)
package_quantity = float(value_attributes.get("package_quantity", {}).get('value', 0.0))

unit_size = float(value_attributes.get("unit_size", {}).get('value', ""))
net_weight_raw = value_attributes.get("net_weight", {})
net_weight = float(net_weight_raw.get('value', 0.0))
#pdb.set_trace()


extracted_data = {
    "allergens": allergens,
    "sku": sku,
    "vegan": vegan,
    "kosher": kosher,
    "organic": organic,
    "vegetarian": vegetarian,
    "gluten_free": gluten_free,
    "lactose_free": lactose_free,
    "package_quantity": package_quantity,
    "unit_size": unit_size,
    "net_weight": net_weight
}

#Archivo de salida CSV
output_csv = "output-product.csv"

#guarda el csv 
with open(output_csv, mode="w", newline="", encoding="utf-8") as file:
    fieldnames = ["allergens", "sku", "vegan", "kosher", "organic", "vegetarian", "gluten_free", "lactose_free", "package_quantity", "unit_size", "net_weight"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow(extracted_data)


driver.quit()

print(f"Archivo csv generado en: {output_csv}")
