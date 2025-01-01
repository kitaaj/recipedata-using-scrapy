import scrapy
import json
from southernlivingrecipes.recipes.livingrecipe import recipe_from_dict



class SouthernlivingSpider(scrapy.spiders.SitemapSpider):
    name = "southernliving"
    sitemap_urls=[
        "https://www.southernliving.com/sitemap_1.xml",
        "https://www.southernliving.com/sitemap_2.xml"
    ]

    def parse(self, response):
        script = response.css('script[type="application/ld+json"]::text').get()
        if script is None:
            return
        
        recipes = recipe_from_dict(json.loads(script))

        for recipe in recipes:
            if 'Recipe' in recipe.type:
                yield{
                    "url": response.url,
                    "name": recipe.name,
                    "image": recipe.image.url,
                    "description": recipe.description,
                    "recipe_category": recipe.recipe_category,
                    "recipe_cuisine": recipe.recipe_cuisine,
                    "recipe_ingredient": recipe.recipe_ingredient,
                    "recipe_instructions": ''.join(instruction.text for instruction in recipe.recipe_instructions),
                    "recipe_yield": recipe.recipe_yield,
                    "total_time": recipe.total_time,
                    "date_published": recipe.date_published,
                    "date_modified": recipe.date_modified,
                    }
