const codeBarreInput = document.getElementById("code-barre-input");
const submitButton = document.getElementById("submit-button");
const productCard = document.getElementById("product-card");
const productName = document.getElementById("product-name");
const productBrand = document.getElementById("product-brand");
const productIngredients = document.getElementById("product-ingredients");

submitButton.addEventListener("click", () => {
  const codeBarre = codeBarreInput.value;
  fetch(`https://world.openfoodfacts.org/api/v0/product/${codeBarre}`)
    .then(response => response.json())
    .then(data => {
      productName.textContent = data.product.product_name;
      productBrand.textContent = data.product.brands;
      productIngredients.textContent = data.product.ingredients_text;
      productCard.style.display = "block";
    })
    .catch(error => {
      console.error(error);
    });
});
