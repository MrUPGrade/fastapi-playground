export FA_DB_URI="postgresql+psycopg2://user:pass@localhost:22222/db"
export FA_CACHE_URI="redis:22223"

env | grep FA_ > .env
