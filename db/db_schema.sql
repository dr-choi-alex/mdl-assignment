CREATE TABLE "users" (
  "id" SERIAL PRIMARY KEY,
  "login_id" varchar unique,
  "password" varchar NOT NULL,
  "email" varchar,
  "full_name" varchar,
  "type" int,
  "created_at" timestamp DEFAULT (now())
);

CREATE INDEX "idx_users_login_id" ON "users" ("login_id");

CREATE TABLE "products" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "img_addr" varchar,
  "description" varchar,
  "price" int,
  "created_at" timestamp DEFAULT (now())
);


CREATE TABLE "carts" (
  "user_id" int NOT NULL,
  "product_id" int,
  "quantity" int
);
CREATE INDEX "idx_carts_user_id" ON "carts" ("user_id");
CREATE INDEX "idx_carts_user_id_product_id" ON "carts" ("user_id", "product_id");

ALTER TABLE "carts" ADD UNIQUE ("user_id", "product_id");

ALTER TABLE "carts" ADD FOREIGN KEY ("product_id") REFERENCES "products" ("id") on delete cascade;

ALTER TABLE "carts" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id")  on delete cascade;





