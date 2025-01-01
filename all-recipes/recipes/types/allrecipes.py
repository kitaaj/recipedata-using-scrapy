from typing import Optional, Any, List, TypeVar, Type, cast, Callable
from datetime import datetime
import dateutil.parser


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


class AggregateRating:
    type: Optional[str]
    rating_value: Optional[str]
    rating_count: Optional[int]

    def __init__(self, type: Optional[str], rating_value: Optional[str], rating_count: Optional[int]) -> None:
        self.type = type
        self.rating_value = rating_value
        self.rating_count = rating_count

    @staticmethod
    def from_dict(obj: Any) -> 'AggregateRating':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("@type"))
        rating_value = from_union([from_str, from_none], obj.get("ratingValue"))
        rating_count = from_union([from_none, lambda x: int(from_str(x))], obj.get("ratingCount"))
        return AggregateRating(type, rating_value, rating_count)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.type is not None:
            result["@type"] = from_union([from_str, from_none], self.type)
        if self.rating_value is not None:
            result["ratingValue"] = from_union([from_str, from_none], self.rating_value)
        if self.rating_count is not None:
            result["ratingCount"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.rating_count)
        return result


class AuthorElement:
    type: Optional[str]
    name: Optional[str]
    url: Optional[str]

    def __init__(self, type: Optional[str], name: Optional[str], url: Optional[str]) -> None:
        self.type = type
        self.name = name
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'AuthorElement':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("@type"))
        name = from_union([from_str, from_none], obj.get("name"))
        url = from_union([from_str, from_none], obj.get("url"))
        return AuthorElement(type, name, url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.type is not None:
            result["@type"] = from_union([from_str, from_none], self.type)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        return result


class Image:
    type: Optional[str]
    url: Optional[str]
    height: Optional[int]
    width: Optional[int]

    def __init__(self, type: Optional[str], url: Optional[str], height: Optional[int], width: Optional[int]) -> None:
        self.type = type
        self.url = url
        self.height = height
        self.width = width

    @staticmethod
    def from_dict(obj: Any) -> 'Image':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("@type"))
        url = from_union([from_str, from_none], obj.get("url"))
        height = from_union([from_int, from_none], obj.get("height"))
        width = from_union([from_int, from_none], obj.get("width"))
        return Image(type, url, height, width)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.type is not None:
            result["@type"] = from_union([from_str, from_none], self.type)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.height is not None:
            result["height"] = from_union([from_int, from_none], self.height)
        if self.width is not None:
            result["width"] = from_union([from_int, from_none], self.width)
        return result


class Item:
    id: Optional[str]
    name: Optional[str]

    def __init__(self, id: Optional[str], name: Optional[str]) -> None:
        self.id = id
        self.name = name

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("@id"))
        name = from_union([from_str, from_none], obj.get("name"))
        return Item(id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["@id"] = from_union([from_str, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        return result


class ItemListElement:
    type: Optional[str]
    position: Optional[int]
    item: Optional[Item]

    def __init__(self, type: Optional[str], position: Optional[int], item: Optional[Item]) -> None:
        self.type = type
        self.position = position
        self.item = item

    @staticmethod
    def from_dict(obj: Any) -> 'ItemListElement':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("@type"))
        position = from_union([from_int, from_none], obj.get("position"))
        item = from_union([Item.from_dict, from_none], obj.get("item"))
        return ItemListElement(type, position, item)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.type is not None:
            result["@type"] = from_union([from_str, from_none], self.type)
        if self.position is not None:
            result["position"] = from_union([from_int, from_none], self.position)
        if self.item is not None:
            result["item"] = from_union([lambda x: to_class(Item, x), from_none], self.item)
        return result


class Breadcrumb:
    type: Optional[str]
    item_list_element: Optional[List[ItemListElement]]

    def __init__(self, type: Optional[str], item_list_element: Optional[List[ItemListElement]]) -> None:
        self.type = type
        self.item_list_element = item_list_element

    @staticmethod
    def from_dict(obj: Any) -> 'Breadcrumb':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("@type"))
        item_list_element = from_union([lambda x: from_list(ItemListElement.from_dict, x), from_none], obj.get("itemListElement"))
        return Breadcrumb(type, item_list_element)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.type is not None:
            result["@type"] = from_union([from_str, from_none], self.type)
        if self.item_list_element is not None:
            result["itemListElement"] = from_union([lambda x: from_list(lambda x: to_class(ItemListElement, x), x), from_none], self.item_list_element)
        return result


class MainEntityOfPage:
    type: Optional[List[str]]
    id: Optional[str]
    breadcrumb: Optional[Breadcrumb]

    def __init__(self, type: Optional[List[str]], id: Optional[str], breadcrumb: Optional[Breadcrumb]) -> None:
        self.type = type
        self.id = id
        self.breadcrumb = breadcrumb

    @staticmethod
    def from_dict(obj: Any) -> 'MainEntityOfPage':
        assert isinstance(obj, dict)
        type = from_union([lambda x: from_list(from_str, x), from_none], obj.get("@type"))
        id = from_union([from_str, from_none], obj.get("@id"))
        breadcrumb = from_union([Breadcrumb.from_dict, from_none], obj.get("breadcrumb"))
        return MainEntityOfPage(type, id, breadcrumb)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.type is not None:
            result["@type"] = from_union([lambda x: from_list(from_str, x), from_none], self.type)
        if self.id is not None:
            result["@id"] = from_union([from_str, from_none], self.id)
        if self.breadcrumb is not None:
            result["breadcrumb"] = from_union([lambda x: to_class(Breadcrumb, x), from_none], self.breadcrumb)
        return result


class Nutrition:
    type: Optional[str]
    calories: Optional[str]
    carbohydrate_content: Optional[str]
    cholesterol_content: Optional[str]
    fiber_content: Optional[str]
    protein_content: Optional[str]
    saturated_fat_content: Optional[str]
    sodium_content: Optional[str]
    sugar_content: Optional[str]
    fat_content: Optional[str]
    unsaturated_fat_content: Optional[str]

    def __init__(self, type: Optional[str], calories: Optional[str], carbohydrate_content: Optional[str], cholesterol_content: Optional[str], fiber_content: Optional[str], protein_content: Optional[str], saturated_fat_content: Optional[str], sodium_content: Optional[str], sugar_content: Optional[str], fat_content: Optional[str], unsaturated_fat_content: Optional[str]) -> None:
        self.type = type
        self.calories = calories
        self.carbohydrate_content = carbohydrate_content
        self.cholesterol_content = cholesterol_content
        self.fiber_content = fiber_content
        self.protein_content = protein_content
        self.saturated_fat_content = saturated_fat_content
        self.sodium_content = sodium_content
        self.sugar_content = sugar_content
        self.fat_content = fat_content
        self.unsaturated_fat_content = unsaturated_fat_content

    @staticmethod
    def from_dict(obj: Any) -> 'Nutrition':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("@type"))
        calories = from_union([from_str, from_none], obj.get("calories"))
        carbohydrate_content = from_union([from_str, from_none], obj.get("carbohydrateContent"))
        cholesterol_content = from_union([from_str, from_none], obj.get("cholesterolContent"))
        fiber_content = from_union([from_str, from_none], obj.get("fiberContent"))
        protein_content = from_union([from_str, from_none], obj.get("proteinContent"))
        saturated_fat_content = from_union([from_str, from_none], obj.get("saturatedFatContent"))
        sodium_content = from_union([from_str, from_none], obj.get("sodiumContent"))
        sugar_content = from_union([from_str, from_none], obj.get("sugarContent"))
        fat_content = from_union([from_str, from_none], obj.get("fatContent"))
        unsaturated_fat_content = from_union([from_str, from_none], obj.get("unsaturatedFatContent"))
        return Nutrition(type, calories, carbohydrate_content, cholesterol_content, fiber_content, protein_content, saturated_fat_content, sodium_content, sugar_content, fat_content, unsaturated_fat_content)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.type is not None:
            result["@type"] = from_union([from_str, from_none], self.type)
        if self.calories is not None:
            result["calories"] = from_union([from_str, from_none], self.calories)
        if self.carbohydrate_content is not None:
            result["carbohydrateContent"] = from_union([from_str, from_none], self.carbohydrate_content)
        if self.cholesterol_content is not None:
            result["cholesterolContent"] = from_union([from_str, from_none], self.cholesterol_content)
        if self.fiber_content is not None:
            result["fiberContent"] = from_union([from_str, from_none], self.fiber_content)
        if self.protein_content is not None:
            result["proteinContent"] = from_union([from_str, from_none], self.protein_content)
        if self.saturated_fat_content is not None:
            result["saturatedFatContent"] = from_union([from_str, from_none], self.saturated_fat_content)
        if self.sodium_content is not None:
            result["sodiumContent"] = from_union([from_str, from_none], self.sodium_content)
        if self.sugar_content is not None:
            result["sugarContent"] = from_union([from_str, from_none], self.sugar_content)
        if self.fat_content is not None:
            result["fatContent"] = from_union([from_str, from_none], self.fat_content)
        if self.unsaturated_fat_content is not None:
            result["unsaturatedFatContent"] = from_union([from_str, from_none], self.unsaturated_fat_content)
        return result


class Publisher:
    type: Optional[str]
    name: Optional[str]
    url: Optional[str]
    logo: Optional[Image]
    brand: Optional[str]
    publishing_principles: Optional[str]
    same_as: Optional[List[str]]

    def __init__(self, type: Optional[str], name: Optional[str], url: Optional[str], logo: Optional[Image], brand: Optional[str], publishing_principles: Optional[str], same_as: Optional[List[str]]) -> None:
        self.type = type
        self.name = name
        self.url = url
        self.logo = logo
        self.brand = brand
        self.publishing_principles = publishing_principles
        self.same_as = same_as

    @staticmethod
    def from_dict(obj: Any) -> 'Publisher':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("@type"))
        name = from_union([from_str, from_none], obj.get("name"))
        url = from_union([from_str, from_none], obj.get("url"))
        logo = from_union([Image.from_dict, from_none], obj.get("logo"))
        brand = from_union([from_str, from_none], obj.get("brand"))
        publishing_principles = from_union([from_str, from_none], obj.get("publishingPrinciples"))
        same_as = from_union([lambda x: from_list(from_str, x), from_none], obj.get("sameAs"))
        return Publisher(type, name, url, logo, brand, publishing_principles, same_as)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.type is not None:
            result["@type"] = from_union([from_str, from_none], self.type)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.logo is not None:
            result["logo"] = from_union([lambda x: to_class(Image, x), from_none], self.logo)
        if self.brand is not None:
            result["brand"] = from_union([from_str, from_none], self.brand)
        if self.publishing_principles is not None:
            result["publishingPrinciples"] = from_union([from_str, from_none], self.publishing_principles)
        if self.same_as is not None:
            result["sameAs"] = from_union([lambda x: from_list(from_str, x), from_none], self.same_as)
        return result


class RecipeInstruction:
    type: Optional[str]
    text: Optional[str]

    def __init__(self, type: Optional[str], text: Optional[str]) -> None:
        self.type = type
        self.text = text

    @staticmethod
    def from_dict(obj: Any) -> 'RecipeInstruction':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("@type"))
        text = from_union([from_str, from_none], obj.get("text"))
        return RecipeInstruction(type, text)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.type is not None:
            result["@type"] = from_union([from_str, from_none], self.type)
        if self.text is not None:
            result["text"] = from_union([from_str, from_none], self.text)
        return result


class ReviewAuthor:
    type: Optional[str]
    name: Optional[str]

    def __init__(self, type: Optional[str], name: Optional[str]) -> None:
        self.type = type
        self.name = name

    @staticmethod
    def from_dict(obj: Any) -> 'ReviewAuthor':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("@type"))
        name = from_union([from_str, from_none], obj.get("name"))
        return ReviewAuthor(type, name)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.type is not None:
            result["@type"] = from_union([from_str, from_none], self.type)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        return result


class ReviewRating:
    type: Optional[str]
    rating_value: Optional[int]

    def __init__(self, type: Optional[str], rating_value: Optional[int]) -> None:
        self.type = type
        self.rating_value = rating_value

    @staticmethod
    def from_dict(obj: Any) -> 'ReviewRating':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("@type"))
        rating_value = from_union([from_none, lambda x: int(from_str(x))], obj.get("ratingValue"))
        return ReviewRating(type, rating_value)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.type is not None:
            result["@type"] = from_union([from_str, from_none], self.type)
        if self.rating_value is not None:
            result["ratingValue"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.rating_value)
        return result


class Review:
    type: Optional[str]
    review_rating: Optional[ReviewRating]
    author: Optional[ReviewAuthor]
    review_body: Optional[str]

    def __init__(self, type: Optional[str], review_rating: Optional[ReviewRating], author: Optional[ReviewAuthor], review_body: Optional[str]) -> None:
        self.type = type
        self.review_rating = review_rating
        self.author = author
        self.review_body = review_body

    @staticmethod
    def from_dict(obj: Any) -> 'Review':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("@type"))
        review_rating = from_union([ReviewRating.from_dict, from_none], obj.get("reviewRating"))
        author = from_union([ReviewAuthor.from_dict, from_none], obj.get("author"))
        review_body = from_union([from_str, from_none], obj.get("reviewBody"))
        return Review(type, review_rating, author, review_body)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.type is not None:
            result["@type"] = from_union([from_str, from_none], self.type)
        if self.review_rating is not None:
            result["reviewRating"] = from_union([lambda x: to_class(ReviewRating, x), from_none], self.review_rating)
        if self.author is not None:
            result["author"] = from_union([lambda x: to_class(ReviewAuthor, x), from_none], self.author)
        if self.review_body is not None:
            result["reviewBody"] = from_union([from_str, from_none], self.review_body)
        return result


class RecipeElement:
    context: Optional[str]
    type: Optional[List[str]]
    headline: Optional[str]
    date_published: Optional[datetime]
    date_modified: Optional[datetime]
    author: Optional[List[AuthorElement]]
    description: Optional[str]
    image: Optional[Image]
    publisher: Optional[Publisher]
    name: Optional[str]
    aggregate_rating: Optional[AggregateRating]
    cook_time: Optional[str]
    nutrition: Optional[Nutrition]
    prep_time: Optional[str]
    recipe_category: Optional[List[str]]
    recipe_cuisine: Optional[List[str]]
    recipe_ingredient: Optional[List[str]]
    recipe_instructions: Optional[List[RecipeInstruction]]
    recipe_yield: Optional[List[int]]
    total_time: Optional[str]
    review: Optional[List[Review]]
    main_entity_of_page: Optional[MainEntityOfPage]
    about: Optional[List[Any]]

    def __init__(self, context: Optional[str], type: Optional[List[str]], headline: Optional[str], date_published: Optional[datetime], date_modified: Optional[datetime], author: Optional[List[AuthorElement]], description: Optional[str], image: Optional[Image], publisher: Optional[Publisher], name: Optional[str], aggregate_rating: Optional[AggregateRating], cook_time: Optional[str], nutrition: Optional[Nutrition], prep_time: Optional[str], recipe_category: Optional[List[str]], recipe_cuisine: Optional[List[str]], recipe_ingredient: Optional[List[str]], recipe_instructions: Optional[List[RecipeInstruction]], recipe_yield: Optional[List[int]], total_time: Optional[str], review: Optional[List[Review]], main_entity_of_page: Optional[MainEntityOfPage], about: Optional[List[Any]]) -> None:
        self.context = context
        self.type = type
        self.headline = headline
        self.date_published = date_published
        self.date_modified = date_modified
        self.author = author
        self.description = description
        self.image = image
        self.publisher = publisher
        self.name = name
        self.aggregate_rating = aggregate_rating
        self.cook_time = cook_time
        self.nutrition = nutrition
        self.prep_time = prep_time
        self.recipe_category = recipe_category
        self.recipe_cuisine = recipe_cuisine
        self.recipe_ingredient = recipe_ingredient
        self.recipe_instructions = recipe_instructions
        self.recipe_yield = recipe_yield
        self.total_time = total_time
        self.review = review
        self.main_entity_of_page = main_entity_of_page
        self.about = about

    @staticmethod
    def from_dict(obj: Any) -> 'RecipeElement':
        assert isinstance(obj, dict)
        context = from_union([from_str, from_none], obj.get("@context"))
        type = from_union([lambda x: from_list(from_str, x), from_none], obj.get("@type"))
        headline = from_union([from_str, from_none], obj.get("headline"))
        date_published = from_union([from_datetime, from_none], obj.get("datePublished"))
        date_modified = from_union([from_datetime, from_none], obj.get("dateModified"))
        author = from_union([lambda x: from_list(AuthorElement.from_dict, x), from_none], obj.get("author"))
        description = from_union([from_str, from_none], obj.get("description"))
        image = from_union([Image.from_dict, from_none], obj.get("image"))
        publisher = from_union([Publisher.from_dict, from_none], obj.get("publisher"))
        name = from_union([from_str, from_none], obj.get("name"))
        aggregate_rating = from_union([AggregateRating.from_dict, from_none], obj.get("aggregateRating"))
        cook_time = from_union([from_str, from_none], obj.get("cookTime"))
        nutrition = from_union([Nutrition.from_dict, from_none], obj.get("nutrition"))
        prep_time = from_union([from_str, from_none], obj.get("prepTime"))
        recipe_category = from_union([lambda x: from_list(from_str, x), from_none], obj.get("recipeCategory"))
        recipe_cuisine = from_union([lambda x: from_list(from_str, x), from_none], obj.get("recipeCuisine"))
        recipe_ingredient = from_union([lambda x: from_list(from_str, x), from_none], obj.get("recipeIngredient"))
        recipe_instructions = from_union([lambda x: from_list(RecipeInstruction.from_dict, x), from_none], obj.get("recipeInstructions"))
        recipe_yield = from_union([lambda x: from_list(lambda x: int(from_str(x)), x), from_none], obj.get("recipeYield"))
        total_time = from_union([from_str, from_none], obj.get("totalTime"))
        review = from_union([lambda x: from_list(Review.from_dict, x), from_none], obj.get("review"))
        main_entity_of_page = from_union([MainEntityOfPage.from_dict, from_none], obj.get("mainEntityOfPage"))
        about = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("about"))
        return RecipeElement(context, type, headline, date_published, date_modified, author, description, image, publisher, name, aggregate_rating, cook_time, nutrition, prep_time, recipe_category, recipe_cuisine, recipe_ingredient, recipe_instructions, recipe_yield, total_time, review, main_entity_of_page, about)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.context is not None:
            result["@context"] = from_union([from_str, from_none], self.context)
        if self.type is not None:
            result["@type"] = from_union([lambda x: from_list(from_str, x), from_none], self.type)
        if self.headline is not None:
            result["headline"] = from_union([from_str, from_none], self.headline)
        if self.date_published is not None:
            result["datePublished"] = from_union([lambda x: x.isoformat(), from_none], self.date_published)
        if self.date_modified is not None:
            result["dateModified"] = from_union([lambda x: x.isoformat(), from_none], self.date_modified)
        if self.author is not None:
            result["author"] = from_union([lambda x: from_list(lambda x: to_class(AuthorElement, x), x), from_none], self.author)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.image is not None:
            result["image"] = from_union([lambda x: to_class(Image, x), from_none], self.image)
        if self.publisher is not None:
            result["publisher"] = from_union([lambda x: to_class(Publisher, x), from_none], self.publisher)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.aggregate_rating is not None:
            result["aggregateRating"] = from_union([lambda x: to_class(AggregateRating, x), from_none], self.aggregate_rating)
        if self.cook_time is not None:
            result["cookTime"] = from_union([from_str, from_none], self.cook_time)
        if self.nutrition is not None:
            result["nutrition"] = from_union([lambda x: to_class(Nutrition, x), from_none], self.nutrition)
        if self.prep_time is not None:
            result["prepTime"] = from_union([from_str, from_none], self.prep_time)
        if self.recipe_category is not None:
            result["recipeCategory"] = from_union([lambda x: from_list(from_str, x), from_none], self.recipe_category)
        if self.recipe_cuisine is not None:
            result["recipeCuisine"] = from_union([lambda x: from_list(from_str, x), from_none], self.recipe_cuisine)
        if self.recipe_ingredient is not None:
            result["recipeIngredient"] = from_union([lambda x: from_list(from_str, x), from_none], self.recipe_ingredient)
        if self.recipe_instructions is not None:
            result["recipeInstructions"] = from_union([lambda x: from_list(lambda x: to_class(RecipeInstruction, x), x), from_none], self.recipe_instructions)
        if self.recipe_yield is not None:
            result["recipeYield"] = from_union([lambda x: from_list(lambda x: from_str((lambda x: str(x))(x)), x), from_none], self.recipe_yield)
        if self.total_time is not None:
            result["totalTime"] = from_union([from_str, from_none], self.total_time)
        if self.review is not None:
            result["review"] = from_union([lambda x: from_list(lambda x: to_class(Review, x), x), from_none], self.review)
        if self.main_entity_of_page is not None:
            result["mainEntityOfPage"] = from_union([lambda x: to_class(MainEntityOfPage, x), from_none], self.main_entity_of_page)
        if self.about is not None:
            result["about"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.about)
        return result


def recipe_from_dict(s: Any) -> List[RecipeElement]:
    return from_list(RecipeElement.from_dict, s)


def recipe_to_dict(x: List[RecipeElement]) -> Any:
    return from_list(lambda x: to_class(RecipeElement, x), x)
