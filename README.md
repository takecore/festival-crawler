## Docker イメージの作成

```sh
docker build -t festival-crawler-app .
```

## Docker コンテナの起動

```sh
# ワーキングディレクトリ直下で実行
docker run -itd -v $(pwd)/app:/usr/src/app \
           --name festival-crawler-app \
           festival-crawler-app
```

## コンテナへログイン

```
docker exec -it festival-crawler-app /bin/sh
```

## スクレイピングコマンド

```
scrapy crawl festival:august -o result.json
```
