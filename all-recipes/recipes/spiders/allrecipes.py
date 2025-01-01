import scrapy
import json
from recipes.types.allrecipes import recipe_from_dict


class AllrecipesSpider(scrapy.spiders.SitemapSpider):
    name = "allrecipes"
    

    sitemap_urls = [
        "https://www.allrecipes.com/sitemap_1.xml",
        "https://www.allrecipes.com/sitemap_2.xml",
        "https://www.allrecipes.com/sitemap_3.xml",
        "https://www.allrecipes.com/sitemap_4.xml",
    ]

    def parse(self, response):
        script = response.css('script[type="application/ld+json"]::text').get()
        if script is None:
            return
        
        recipes = recipe_from_dict(json.loads(script))

        for recipe in recipes:
            #if recipe.type != "Recipe":
                #return
            if not recipe.nutrition:
                return
            if not recipe.aggregate_rating:
                return
            yield {
    "url": response.url,
    "title": recipe.name,
    "image": recipe.image.url,
    "description": recipe.description,
    "publisher": recipe.publisher.name,
    "date_published": recipe.date_published,
    "date_modified": recipe.date_modified,
    "rating_value": recipe.aggregate_rating.rating_value,
    "rating_count": recipe.aggregate_rating.rating_count,
    "recipe_category": recipe.recipe_category,
    "recipe_cuisine": recipe.recipe_cuisine,
    "prep_time": recipe.prep_time,
    "cook_time": recipe.cook_time,
    "total_time": recipe.total_time,
    "recipe_ingredient": recipe.recipe_ingredient,
    "recipe_instructions": ''.join(instruction.text for instruction in recipe.recipe_instructions),
    "recipe_yield": recipe.recipe_yield,
    "nutrition": {
        "calories": strip_number_from_text(recipe.nutrition.calories),
        "carbohydrate_content": strip_number_from_text(recipe.nutrition.carbohydrate_content),
        "cholesterol_content": strip_number_from_text(recipe.nutrition.cholesterol_content),
        "fiber_content": strip_number_from_text(recipe.nutrition.fiber_content),
        "protein_content": strip_number_from_text(recipe.nutrition.protein_content),
        "saturated_fat_content": strip_number_from_text(recipe.nutrition.saturated_fat_content),
        "sodium_content": strip_number_from_text(recipe.nutrition.sodium_content),
        "sugar_content": strip_number_from_text(recipe.nutrition.sugar_content),
        "fat_content": strip_number_from_text(recipe.nutrition.fat_content),
        "unsaturated_fat_content": strip_number_from_text(recipe.nutrition.unsaturated_fat_content),
    }
}


def strip_number_from_text(text):
    return int(text.split(" ")[0])
