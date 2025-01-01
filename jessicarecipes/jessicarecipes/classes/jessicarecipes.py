from typing import Optional, Any, List, Union, TypeVar, Type, Callable, cast
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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


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


class Author:
    name: Optional[str]
    id: Optional[str]

    def __init__(self, name: Optional[str], id: Optional[str]) -> None:
        self.name = name
        self.id = id

    @staticmethod
    def from_dict(obj: Any) -> 'Author':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        id = from_union([from_str, from_none], obj.get("@id"))
        return Author(name, id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.id is not None:
            result["@id"] = from_union([from_str, from_none], self.id)
        return result


class Breadcrumb:
    id: Optional[str]

    def __init__(self, id: Optional[str]) -> None:
        self.id = id

    @staticmethod
    def from_dict(obj: Any) -> 'Breadcrumb':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("@id"))
        return Breadcrumb(id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["@id"] = from_union([from_str, from_none], self.id)
        return result


class ImageClass:
    id: Optional[str]
    type: Optional[str]
    in_language: Optional[str]
    url: Optional[str]
    content_url: Optional[str]
    caption: Optional[str]
    width: Optional[int]
    height: Optional[int]

    def __init__(self, id: Optional[str], type: Optional[str], in_language: Optional[str], url: Optional[str], content_url: Optional[str], caption: Optional[str], width: Optional[int], height: Optional[int]) -> None:
        self.id = id
        self.type = type
        self.in_language = in_language
        self.url = url
        self.content_url = content_url
        self.caption = caption
        self.width = width
        self.height = height

    @staticmethod
    def from_dict(obj: Any) -> 'ImageClass':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("@id"))
        type = from_union([from_str, from_none], obj.get("@type"))
        in_language = from_union([from_str, from_none], obj.get("inLanguage"))
        url = from_union([from_str, from_none], obj.get("url"))
        content_url = from_union([from_str, from_none], obj.get("contentUrl"))
        caption = from_union([from_str, from_none], obj.get("caption"))
        width = from_union([from_int, from_none], obj.get("width"))
        height = from_union([from_int, from_none], obj.get("height"))
        return ImageClass(id, type, in_language, url, content_url, caption, width, height)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["@id"] = from_union([from_str, from_none], self.id)
        if self.type is not None:
            result["@type"] = from_union([from_str, from_none], self.type)
        if self.in_language is not None:
            result["inLanguage"] = from_union([from_str, from_none], self.in_language)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.content_url is not None:
            result["contentUrl"] = from_union([from_str, from_none], self.content_url)
        if self.caption is not None:
            result["caption"] = from_union([from_str, from_none], self.caption)
        if self.width is not None:
            result["width"] = from_union([from_int, from_none], self.width)
        if self.height is not None:
            result["height"] = from_union([from_int, from_none], self.height)
        return result


class ItemListElement:
    type: Optional[str]
    position: Optional[int]
    name: Optional[str]
    item: Optional[str]

    def __init__(self, type: Optional[str], position: Optional[int], name: Optional[str], item: Optional[str]) -> None:
        self.type = type
        self.position = position
        self.name = name
        self.item = item

    @staticmethod
    def from_dict(obj: Any) -> 'ItemListElement':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("@type"))
        position = from_union([from_int, from_none], obj.get("position"))
        name = from_union([from_str, from_none], obj.get("name"))
        item = from_union([from_str, from_none], obj.get("item"))
        return ItemListElement(type, position, name, item)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.type is not None:
            result["@type"] = from_union([from_str, from_none], self.type)
        if self.position is not None:
            result["position"] = from_union([from_int, from_none], self.position)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.item is not None:
            result["item"] = from_union([from_str, from_none], self.item)
        return result


class Nutrition:
    type: Optional[str]
    calories: Optional[str]
    carbohydrate_content: Optional[str]
    protein_content: Optional[str]
    fat_content: Optional[str]
    saturated_fat_content: Optional[str]
    cholesterol_content: Optional[str]
    sodium_content: Optional[str]
    fiber_content: Optional[str]
    sugar_content: Optional[str]
    unsaturated_fat_content: Optional[str]
    serving_size: Optional[str]

    def __init__(self, type: Optional[str], calories: Optional[str], carbohydrate_content: Optional[str], protein_content: Optional[str], fat_content: Optional[str], saturated_fat_content: Optional[str], cholesterol_content: Optional[str], sodium_content: Optional[str], fiber_content: Optional[str], sugar_content: Optional[str], unsaturated_fat_content: Optional[str], serving_size: Optional[str]) -> None:
        self.type = type
        self.calories = calories
        self.carbohydrate_content = carbohydrate_content
        self.protein_content = protein_content
        self.fat_content = fat_content
        self.saturated_fat_content = saturated_fat_content
        self.cholesterol_content = cholesterol_content
        self.sodium_content = sodium_content
        self.fiber_content = fiber_content
        self.sugar_content = sugar_content
        self.unsaturated_fat_content = unsaturated_fat_content
        self.serving_size = serving_size

    @staticmethod
    def from_dict(obj: Any) -> 'Nutrition':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("@type"))
        calories = from_union([from_str, from_none], obj.get("calories"))
        carbohydrate_content = from_union([from_str, from_none], obj.get("carbohydrateContent"))
        protein_content = from_union([from_str, from_none], obj.get("proteinContent"))
        fat_content = from_union([from_str, from_none], obj.get("fatContent"))
        saturated_fat_content = from_union([from_str, from_none], obj.get("saturatedFatContent"))
        cholesterol_content = from_union([from_str, from_none], obj.get("cholesterolContent"))
        sodium_content = from_union([from_str, from_none], obj.get("sodiumContent"))
        fiber_content = from_union([from_str, from_none], obj.get("fiberContent"))
        sugar_content = from_union([from_str, from_none], obj.get("sugarContent"))
        unsaturated_fat_content = from_union([from_str, from_none], obj.get("unsaturatedFatContent"))
        serving_size = from_union([from_str, from_none], obj.get("servingSize"))
        return Nutrition(type, calories, carbohydrate_content, protein_content, fat_content, saturated_fat_content, cholesterol_content, sodium_content, fiber_content, sugar_content, unsaturated_fat_content, serving_size)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.type is not None:
            result["@type"] = from_union([from_str, from_none], self.type)
        if self.calories is not None:
            result["calories"] = from_union([from_str, from_none], self.calories)
        if self.carbohydrate_content is not None:
            result["carbohydrateContent"] = from_union([from_str, from_none], self.carbohydrate_content)
        if self.protein_content is not None:
            result["proteinContent"] = from_union([from_str, from_none], self.protein_content)
        if self.fat_content is not None:
            result["fatContent"] = from_union([from_str, from_none], self.fat_content)
        if self.saturated_fat_content is not None:
            result["saturatedFatContent"] = from_union([from_str, from_none], self.saturated_fat_content)
        if self.cholesterol_content is not None:
            result["cholesterolContent"] = from_union([from_str, from_none], self.cholesterol_content)
        if self.sodium_content is not None:
            result["sodiumContent"] = from_union([from_str, from_none], self.sodium_content)
        if self.fiber_content is not None:
            result["fiberContent"] = from_union([from_str, from_none], self.fiber_content)
        if self.sugar_content is not None:
            result["sugarContent"] = from_union([from_str, from_none], self.sugar_content)
        if self.unsaturated_fat_content is not None:
            result["unsaturatedFatContent"] = from_union([from_str, from_none], self.unsaturated_fat_content)
        if self.serving_size is not None:
            result["servingSize"] = from_union([from_str, from_none], self.serving_size)
        return result


class TargetClass:
    type: Optional[str]
    url_template: Optional[str]

    def __init__(self, type: Optional[str], url_template: Optional[str]) -> None:
        self.type = type
        self.url_template = url_template

    @staticmethod
    def from_dict(obj: Any) -> 'TargetClass':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("@type"))
        url_template = from_union([from_str, from_none], obj.get("urlTemplate"))
        return TargetClass(type, url_template)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.type is not None:
            result["@type"] = from_union([from_str, from_none], self.type)
        if self.url_template is not None:
            result["urlTemplate"] = from_union([from_str, from_none], self.url_template)
        return result


class PotentialAction:
    type: Optional[str]
    name: Optional[str]
    target: Optional[Union[List[str], TargetClass]]
    query_input: Optional[str]

    def __init__(self, type: Optional[str], name: Optional[str], target: Optional[Union[List[str], TargetClass]], query_input: Optional[str]) -> None:
        self.type = type
        self.name = name
        self.target = target
        self.query_input = query_input

    @staticmethod
    def from_dict(obj: Any) -> 'PotentialAction':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("@type"))
        name = from_union([from_str, from_none], obj.get("name"))
        target = from_union([lambda x: from_list(from_str, x), TargetClass.from_dict, from_none], obj.get("target"))
        query_input = from_union([from_str, from_none], obj.get("query-input"))
        return PotentialAction(type, name, target, query_input)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.type is not None:
            result["@type"] = from_union([from_str, from_none], self.type)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.target is not None:
            result["target"] = from_union([lambda x: from_list(from_str, x), lambda x: to_class(TargetClass, x), from_none], self.target)
        if self.query_input is not None:
            result["query-input"] = from_union([from_str, from_none], self.query_input)
        return result


class RecipeInstruction:
    type: Optional[str]
    text: Optional[str]
    name: Optional[str]
    url: Optional[str]

    def __init__(self, type: Optional[str], text: Optional[str], name: Optional[str], url: Optional[str]) -> None:
        self.type = type
        self.text = text
        self.name = name
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'RecipeInstruction':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("@type"))
        text = from_union([from_str, from_none], obj.get("text"))
        name = from_union([from_str, from_none], obj.get("name"))
        url = from_union([from_str, from_none], obj.get("url"))
        return RecipeInstruction(type, text, name, url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.type is not None:
            result["@type"] = from_union([from_str, from_none], self.type)
        if self.text is not None:
            result["text"] = from_union([from_str, from_none], self.text)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        return result


class Video:
    name: Optional[str]
    description: Optional[str]
    upload_date: Optional[datetime]
    duration: Optional[str]
    thumbnail_url: Optional[str]
    embed_url: Optional[str]
    content_url: Optional[str]
    type: Optional[str]

    def __init__(self, name: Optional[str], description: Optional[str], upload_date: Optional[datetime], duration: Optional[str], thumbnail_url: Optional[str], embed_url: Optional[str], content_url: Optional[str], type: Optional[str]) -> None:
        self.name = name
        self.description = description
        self.upload_date = upload_date
        self.duration = duration
        self.thumbnail_url = thumbnail_url
        self.embed_url = embed_url
        self.content_url = content_url
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Video':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        description = from_union([from_str, from_none], obj.get("description"))
        upload_date = from_union([from_datetime, from_none], obj.get("uploadDate"))
        duration = from_union([from_str, from_none], obj.get("duration"))
        thumbnail_url = from_union([from_str, from_none], obj.get("thumbnailUrl"))
        embed_url = from_union([from_str, from_none], obj.get("embedUrl"))
        content_url = from_union([from_str, from_none], obj.get("contentUrl"))
        type = from_union([from_str, from_none], obj.get("@type"))
        return Video(name, description, upload_date, duration, thumbnail_url, embed_url, content_url, type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.upload_date is not None:
            result["uploadDate"] = from_union([lambda x: x.isoformat(), from_none], self.upload_date)
        if self.duration is not None:
            result["duration"] = from_union([from_str, from_none], self.duration)
        if self.thumbnail_url is not None:
            result["thumbnailUrl"] = from_union([from_str, from_none], self.thumbnail_url)
        if self.embed_url is not None:
            result["embedUrl"] = from_union([from_str, from_none], self.embed_url)
        if self.content_url is not None:
            result["contentUrl"] = from_union([from_str, from_none], self.content_url)
        if self.type is not None:
            result["@type"] = from_union([from_str, from_none], self.type)
        return result


class Graph:
    type: Optional[str]
    id: Optional[str]
    is_part_of: Optional[Breadcrumb]
    author: Optional[Author]
    headline: Optional[str]
    date_published: Optional[datetime]
    date_modified: Optional[datetime]
    word_count: Optional[int]
    comment_count: Optional[int]
    publisher: Optional[Breadcrumb]
    image: Optional[Union[ImageClass, List[str]]]
    thumbnail_url: Optional[str]
    keywords: Optional[Union[List[str], str]]
    article_section: Optional[List[str]]
    in_language: Optional[str]
    potential_action: Optional[List[PotentialAction]]
    url: Optional[str]
    name: Optional[str]
    primary_image_of_page: Optional[Breadcrumb]
    description: Optional[str]
    breadcrumb: Optional[Breadcrumb]
    content_url: Optional[str]
    width: Optional[int]
    height: Optional[int]
    item_list_element: Optional[List[ItemListElement]]
    logo: Optional[ImageClass]
    same_as: Optional[List[str]]
    video: Optional[Video]
    recipe_yield: Optional[List[str]]
    prep_time: Optional[str]
    total_time: Optional[str]
    recipe_ingredient: Optional[List[str]]
    recipe_instructions: Optional[List[RecipeInstruction]]
    aggregate_rating: Optional[AggregateRating]
    recipe_category: Optional[List[str]]
    recipe_cuisine: Optional[List[str]]
    nutrition: Optional[Nutrition]
    main_entity_of_page: Optional[str]

    def __init__(self, type: Optional[str], id: Optional[str], is_part_of: Optional[Breadcrumb], author: Optional[Author], headline: Optional[str], date_published: Optional[datetime], date_modified: Optional[datetime], word_count: Optional[int], comment_count: Optional[int], publisher: Optional[Breadcrumb], image: Optional[Union[ImageClass, List[str]]], thumbnail_url: Optional[str], keywords: Optional[Union[List[str], str]], article_section: Optional[List[str]], in_language: Optional[str], potential_action: Optional[List[PotentialAction]], url: Optional[str], name: Optional[str], primary_image_of_page: Optional[Breadcrumb], description: Optional[str], breadcrumb: Optional[Breadcrumb], content_url: Optional[str], width: Optional[int], height: Optional[int], item_list_element: Optional[List[ItemListElement]], logo: Optional[ImageClass], same_as: Optional[List[str]], video: Optional[Video], recipe_yield: Optional[List[str]], prep_time: Optional[str], total_time: Optional[str], recipe_ingredient: Optional[List[str]], recipe_instructions: Optional[List[RecipeInstruction]], aggregate_rating: Optional[AggregateRating], recipe_category: Optional[List[str]], recipe_cuisine: Optional[List[str]], nutrition: Optional[Nutrition], main_entity_of_page: Optional[str]) -> None:
        self.type = type
        self.id = id
        self.is_part_of = is_part_of
        self.author = author
        self.headline = headline
        self.date_published = date_published
        self.date_modified = date_modified
        self.word_count = word_count
        self.comment_count = comment_count
        self.publisher = publisher
        self.image = image
        self.thumbnail_url = thumbnail_url
        self.keywords = keywords
        self.article_section = article_section
        self.in_language = in_language
        self.potential_action = potential_action
        self.url = url
        self.name = name
        self.primary_image_of_page = primary_image_of_page
        self.description = description
        self.breadcrumb = breadcrumb
        self.content_url = content_url
        self.width = width
        self.height = height
        self.item_list_element = item_list_element
        self.logo = logo
        self.same_as = same_as
        self.video = video
        self.recipe_yield = recipe_yield
        self.prep_time = prep_time
        self.total_time = total_time
        self.recipe_ingredient = recipe_ingredient
        self.recipe_instructions = recipe_instructions
        self.aggregate_rating = aggregate_rating
        self.recipe_category = recipe_category
        self.recipe_cuisine = recipe_cuisine
        self.nutrition = nutrition
        self.main_entity_of_page = main_entity_of_page

    @staticmethod
    def from_dict(obj: Any) -> 'Graph':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("@type"))
        id = from_union([from_str, from_none], obj.get("@id"))
        is_part_of = from_union([Breadcrumb.from_dict, from_none], obj.get("isPartOf"))
        author = from_union([Author.from_dict, from_none], obj.get("author"))
        headline = from_union([from_str, from_none], obj.get("headline"))
        date_published = from_union([from_datetime, from_none], obj.get("datePublished"))
        date_modified = from_union([from_datetime, from_none], obj.get("dateModified"))
        word_count = from_union([from_int, from_none], obj.get("wordCount"))
        comment_count = from_union([from_int, from_none], obj.get("commentCount"))
        publisher = from_union([Breadcrumb.from_dict, from_none], obj.get("publisher"))
        image = from_union([ImageClass.from_dict, lambda x: from_list(from_str, x), from_none], obj.get("image"))
        thumbnail_url = from_union([from_str, from_none], obj.get("thumbnailUrl"))
        keywords = from_union([lambda x: from_list(from_str, x), from_str, from_none], obj.get("keywords"))
        article_section = from_union([lambda x: from_list(from_str, x), from_none], obj.get("articleSection"))
        in_language = from_union([from_str, from_none], obj.get("inLanguage"))
        potential_action = from_union([lambda x: from_list(PotentialAction.from_dict, x), from_none], obj.get("potentialAction"))
        url = from_union([from_str, from_none], obj.get("url"))
        name = from_union([from_str, from_none], obj.get("name"))
        primary_image_of_page = from_union([Breadcrumb.from_dict, from_none], obj.get("primaryImageOfPage"))
        description = from_union([from_str, from_none], obj.get("description"))
        breadcrumb = from_union([Breadcrumb.from_dict, from_none], obj.get("breadcrumb"))
        content_url = from_union([from_str, from_none], obj.get("contentUrl"))
        width = from_union([from_int, from_none], obj.get("width"))
        height = from_union([from_int, from_none], obj.get("height"))
        item_list_element = from_union([lambda x: from_list(ItemListElement.from_dict, x), from_none], obj.get("itemListElement"))
        logo = from_union([ImageClass.from_dict, from_none], obj.get("logo"))
        same_as = from_union([lambda x: from_list(from_str, x), from_none], obj.get("sameAs"))
        video = from_union([Video.from_dict, from_none], obj.get("video"))
        recipe_yield = from_union([lambda x: from_list(from_str, x), from_none], obj.get("recipeYield"))
        prep_time = from_union([from_str, from_none], obj.get("prepTime"))
        total_time = from_union([from_str, from_none], obj.get("totalTime"))
        recipe_ingredient = from_union([lambda x: from_list(from_str, x), from_none], obj.get("recipeIngredient"))
        recipe_instructions = from_union([lambda x: from_list(RecipeInstruction.from_dict, x), from_none], obj.get("recipeInstructions"))
        aggregate_rating = from_union([AggregateRating.from_dict, from_none], obj.get("aggregateRating"))
        recipe_category = from_union([lambda x: from_list(from_str, x), from_none], obj.get("recipeCategory"))
        recipe_cuisine = from_union([lambda x: from_list(from_str, x), from_none], obj.get("recipeCuisine"))
        nutrition = from_union([Nutrition.from_dict, from_none], obj.get("nutrition"))
        main_entity_of_page = from_union([from_str, from_none], obj.get("mainEntityOfPage"))
        return Graph(type, id, is_part_of, author, headline, date_published, date_modified, word_count, comment_count, publisher, image, thumbnail_url, keywords, article_section, in_language, potential_action, url, name, primary_image_of_page, description, breadcrumb, content_url, width, height, item_list_element, logo, same_as, video, recipe_yield, prep_time, total_time, recipe_ingredient, recipe_instructions, aggregate_rating, recipe_category, recipe_cuisine, nutrition, main_entity_of_page)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.type is not None:
            result["@type"] = from_union([from_str, from_none], self.type)
        if self.id is not None:
            result["@id"] = from_union([from_str, from_none], self.id)
        if self.is_part_of is not None:
            result["isPartOf"] = from_union([lambda x: to_class(Breadcrumb, x), from_none], self.is_part_of)
        if self.author is not None:
            result["author"] = from_union([lambda x: to_class(Author, x), from_none], self.author)
        if self.headline is not None:
            result["headline"] = from_union([from_str, from_none], self.headline)
        if self.date_published is not None:
            result["datePublished"] = from_union([lambda x: x.isoformat(), from_none], self.date_published)
        if self.date_modified is not None:
            result["dateModified"] = from_union([lambda x: x.isoformat(), from_none], self.date_modified)
        if self.word_count is not None:
            result["wordCount"] = from_union([from_int, from_none], self.word_count)
        if self.comment_count is not None:
            result["commentCount"] = from_union([from_int, from_none], self.comment_count)
        if self.publisher is not None:
            result["publisher"] = from_union([lambda x: to_class(Breadcrumb, x), from_none], self.publisher)
        if self.image is not None:
            result["image"] = from_union([lambda x: to_class(ImageClass, x), lambda x: from_list(from_str, x), from_none], self.image)
        if self.thumbnail_url is not None:
            result["thumbnailUrl"] = from_union([from_str, from_none], self.thumbnail_url)
        if self.keywords is not None:
            result["keywords"] = from_union([lambda x: from_list(from_str, x), from_str, from_none], self.keywords)
        if self.article_section is not None:
            result["articleSection"] = from_union([lambda x: from_list(from_str, x), from_none], self.article_section)
        if self.in_language is not None:
            result["inLanguage"] = from_union([from_str, from_none], self.in_language)
        if self.potential_action is not None:
            result["potentialAction"] = from_union([lambda x: from_list(lambda x: to_class(PotentialAction, x), x), from_none], self.potential_action)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.primary_image_of_page is not None:
            result["primaryImageOfPage"] = from_union([lambda x: to_class(Breadcrumb, x), from_none], self.primary_image_of_page)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.breadcrumb is not None:
            result["breadcrumb"] = from_union([lambda x: to_class(Breadcrumb, x), from_none], self.breadcrumb)
        if self.content_url is not None:
            result["contentUrl"] = from_union([from_str, from_none], self.content_url)
        if self.width is not None:
            result["width"] = from_union([from_int, from_none], self.width)
        if self.height is not None:
            result["height"] = from_union([from_int, from_none], self.height)
        if self.item_list_element is not None:
            result["itemListElement"] = from_union([lambda x: from_list(lambda x: to_class(ItemListElement, x), x), from_none], self.item_list_element)
        if self.logo is not None:
            result["logo"] = from_union([lambda x: to_class(ImageClass, x), from_none], self.logo)
        if self.same_as is not None:
            result["sameAs"] = from_union([lambda x: from_list(from_str, x), from_none], self.same_as)
        if self.video is not None:
            result["video"] = from_union([lambda x: to_class(Video, x), from_none], self.video)
        if self.recipe_yield is not None:
            result["recipeYield"] = from_union([lambda x: from_list(from_str, x), from_none], self.recipe_yield)
        if self.prep_time is not None:
            result["prepTime"] = from_union([from_str, from_none], self.prep_time)
        if self.total_time is not None:
            result["totalTime"] = from_union([from_str, from_none], self.total_time)
        if self.recipe_ingredient is not None:
            result["recipeIngredient"] = from_union([lambda x: from_list(from_str, x), from_none], self.recipe_ingredient)
        if self.recipe_instructions is not None:
            result["recipeInstructions"] = from_union([lambda x: from_list(lambda x: to_class(RecipeInstruction, x), x), from_none], self.recipe_instructions)
        if self.aggregate_rating is not None:
            result["aggregateRating"] = from_union([lambda x: to_class(AggregateRating, x), from_none], self.aggregate_rating)
        if self.recipe_category is not None:
            result["recipeCategory"] = from_union([lambda x: from_list(from_str, x), from_none], self.recipe_category)
        if self.recipe_cuisine is not None:
            result["recipeCuisine"] = from_union([lambda x: from_list(from_str, x), from_none], self.recipe_cuisine)
        if self.nutrition is not None:
            result["nutrition"] = from_union([lambda x: to_class(Nutrition, x), from_none], self.nutrition)
        if self.main_entity_of_page is not None:
            result["mainEntityOfPage"] = from_union([from_str, from_none], self.main_entity_of_page)
        return result


class Recipe:
    context: Optional[str]
    graph: Optional[List[Graph]]

    def __init__(self, context: Optional[str], graph: Optional[List[Graph]]) -> None:
        self.context = context
        self.graph = graph

    @staticmethod
    def from_dict(obj: Any) -> 'Recipe':
        assert isinstance(obj, dict)
        context = from_union([from_str, from_none], obj.get("@context"))
        graph = from_union([lambda x: from_list(Graph.from_dict, x), from_none], obj.get("@graph"))
        return Recipe(context, graph)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.context is not None:
            result["@context"] = from_union([from_str, from_none], self.context)
        if self.graph is not None:
            result["@graph"] = from_union([lambda x: from_list(lambda x: to_class(Graph, x), x), from_none], self.graph)
        return result


def recipe_from_dict(s: Any) -> Recipe:
    return Recipe.from_dict(s)


def recipe_to_dict(x: Recipe) -> Any:
    return to_class(Recipe, x)
