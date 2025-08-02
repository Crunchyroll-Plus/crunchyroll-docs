getCustomListItems
===========

#### Get items from your custom list.

```http
GET /content/v2/${account_uuid}/custom-lists/${list_id}

# Request Headers
Authorization: Bearer ${TOKEN}
```

| Parameter | Type | Description |
| --- | --- | --- |
| page_size | `int` | Size of the page |
| page | `int` | What page to start searching at |
| sort_by | `manual,date_added` | What to sort the page by |
| order | `asc,desc` | Which order to sort the page by |
