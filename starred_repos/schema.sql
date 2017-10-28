drop table if exists python_repos;
create table python_repos (
  id integer primary key autoincrement,
  repo_id text not null,
  name text not null,
  url text,
  created_date text,
  last_push_date text,
  description text,
  stars text,
  avatar text

);
