""" This will be kept in sync with the corresponding Promoted repos.

Note that the following may not be buildable outside the larger Promoted codebase
context, but is provided for visibility and discussion.

PRs are still welcome and Promoted engineers will be happy to test and iterate,
or refine proposed updates.
"""

CONTENT_FIELDS = {
    #
    # Example of json object path components indicating that from a blob like
    # Item = {"item_name": "Houseplant", "item_properties": {"size": "Gmall, "color": "Green"}}
    # The displayed name in introspectoin will be: "Houseplant Green"
    "content_name_fields": [["item_name"], ["item_properties", "color"]],
    #
    # This template will typically include a formatted token for one or more of the content fields
    # that are synced to the Content Management System, such as the content id to provide links
    # to the marketplace listing itself where that is helpful in analytics interfaces:
    # "content_link_template": "https://samplemarketplace.com/itemlisting/{content_id}/"
    "content_link_template": "https://promoted.ai/",
}
