import cmarkgfm  # type: ignore
from cmarkgfm.cmark import Options as cmarkgfmOptions  # type: ignore


def test_html_wrangling() -> None:
    input_string = """Certainly! Here is an alternative version of the previous code that uses a regular function instead of a lambda function:\n```\n# Sample list of objects\nobjects = [\n    {\"name\": \"obj1\", \"created\": \"2022-01-01\", \"updated\": \"2022-01-02\"},\n    {\"name\": \"obj2\", \"created\": \"2022-01-03\", \"updated\": None},\n    {\"name\": \"obj3\", \"created\": \"2022-01-02\", \"updated\": \"2022-01-04\"},\n    {\"name\": \"obj4\", \"created\": \"2022-01-01\", \"updated\": None},\n]\n\n# Sorting function\ndef get_sort_key(obj):\n    updated = obj.get(\"updated\")\n    return (updated if updated is not None else obj.get(\"created\"), obj[\"name\"])\n\ndef sort_by_updated_or_created(objects):\n    return sorted(objects, key=get_sort_key)\n\n# Sorting the list\nsorted_objects = sort_by_updated_or_created(objects)\n\n# Printing the sorted list\nprint(sorted_objects)\n```\nThis code defines a regular function `get_sort_key` that takes an object as its argument and returns a tuple representing the values to be used for sorting that object. This function is then passed as the `key` argument to the `sorted` function.\n\nThe `get_sort_key` function first retrieves the value of the \"updated\" attribute from the object. If this value is not `None`, it returns a tuple containing this value as its first element and the value of the \"name\" attribute as its second element. If the value of the \"updated\" attribute is `None`, it returns a tuple containing the value of the \"created\" attribute as its first element and the value of the \"name\" attribute as its second element.\n\nThe `sort_by_updated_or_created` function simply calls the `sorted` function with the `get_sort_key` function as its `key` argument.\n\nThe output of this code will be the same as before:\n```\n[\n    {'name': 'obj4', 'created': '2022-01-01', 'updated': None},\n    {'name': 'obj2', 'created': '2022-01-03', 'updated': None},\n    {'name': 'obj1', 'created': '2022-01-01', 'updated': '2022-01-02'},\n    {'name': 'obj3', 'created': '2022-01-02', 'updated': '2022-01-04'}\n]\n```\nThis output shows that the objects are sorted first by the \"updated\" or \"created\" attribute, and if those attributes are the same, they are sorted based on their \"name\" attribute as a secondary key."""

    html = cmarkgfm.github_flavored_markdown_to_html(
        input_string, options=(cmarkgfmOptions.CMARK_OPT_VALIDATE_UTF8)
    )
    print(html)
    assert "<pre>" in html