config = '''{
    "settings" : {
        "index" : {
            "number_of_shards" : 3,
            "number_of_replicas" : 0,
            "analysis" : {
              "filter" : {
                "myNGramFilter" : {
                "type" : "edgeNGram",
                "min_gram" : "1",
                "max_gram" : "30"
                }
              },
              "analyzer" : {
                "myNGramAnalyzer" : {
                  "filter" : [
                    "lowercase",
                    "myNGramFilter"
                  ],
                  "type" : "custom",
                  "tokenizer" : "whitespace"
                },
                "startWith" : {
                  "filter" : "lowercase",
                  "tokenizer" : "keyword"
                }
              }
            }
        }
    },
    "mappings" : {
      "default" : {
        "properties" : {
          "city" : {
            "type" : "text"
          },
          "count_address" : {
            "type" : "long"
          },
          "count_fave" : {
            "type" : "long"
          },
          "count_product" : {
            "type" : "long"
          },
          "count_transaction" : {
            "type" : "long"
          },
          "default_location3" : {
            "type" : "text",
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            }
          },
          "district_id" : {
            "type" : "long"
          },
          "domain" : {
            "type" : "keyword"
          },
          "extended_name" : {
            "type" : "text",
            "fields" : {
              "prefix" : {
                "type" : "text",
                "analyzer" : "myNGramAnalyzer",
                "search_analyzer" : "whitespace"
              }
            }
          },
          "gold_merchant_expired" : {
            "type" : "date"
          },
          "id" : {
            "type" : "long"
          },
          "image_name" : {
            "type" : "keyword",
            "index" : false
          },
          "image_path" : {
            "type" : "keyword",
            "index" : false
          },
          "is_official" : {
            "type" : "boolean"
          },
          "is_power_badge" : {
            "type" : "boolean"
          },
          "is_regular" : {
            "type" : "boolean"
          },
          "location" : {
            "type" : "keyword"
          },
          "name" : {
            "type" : "text",
            "fields" : {
              "prefix" : {
                "type" : "text",
                "analyzer" : "myNGramAnalyzer",
                "search_analyzer" : "whitespace"
              }
            }
          },
          "name_sort" : {
            "type" : "text",
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            }
          },
          "official_brand_image" : {
            "type" : "keyword"
          },
          "official_custom_desc" : {
            "type" : "keyword"
          },
          "official_custom_title" : {
            "type" : "keyword"
          },
          "official_microsite_logo" : {
            "type" : "keyword"
          },
          "official_start_date" : {
            "type" : "date"
          },
          "os_categories" : {
            "type" : "long"
          },
          "os_microsite_logo" : {
            "type" : "text",
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            }
          },
          "os_start" : {
            "type" : "date"
          },
          "owner_id" : {
            "type" : "long"
          },
          "product_images" : {
            "properties" : {
              "image_name" : {
                "type" : "text",
                "fields" : {
                  "keyword" : {
                    "type" : "keyword",
                    "ignore_above" : 256
                  }
                }
              },
              "image_path" : {
                "type" : "text",
                "fields" : {
                  "keyword" : {
                    "type" : "keyword",
                    "ignore_above" : 256
                  }
                }
              },
              "server_id" : {
                "type" : "long"
              }
            }
          },
          "rate_accuracy" : {
            "type" : "float"
          },
          "rate_cancel" : {
            "type" : "float"
          },
          "rate_service" : {
            "type" : "float"
          },
          "rate_speed" : {
            "type" : "float"
          },
          "reputation_score" : {
            "type" : "long"
          },
          "server_id" : {
            "type" : "short",
            "index" : false
          },
          "shipping" : {
            "type" : "long"
          },
          "shop_score" : {
            "type" : "long"
          },
          "short_description" : {
            "type" : "keyword",
            "index" : false
          },
          "status" : {
            "type" : "short"
          },
          "tag_line" : {
            "type" : "keyword",
            "index" : false
          }
        }
      }
    }
}'''