<script setup lang="ts"></script>

<template>
  <router-view />
</template>

<style scoped></style>

initdb.exe -D  -E UTF-8 --locale=chs -U postgres -W

pg_ctl.exe -D J:\ai\PostgreSql\data -l logfile start


pg_ctl.exe register -D J:\ai\PostgreSql\data -N PostgreSQL

pg_ctl status -D J:\ai\PostgreSql\data

pg_ctl start -D J:\ai\PostgreSql\data

psql -U postgres


SELECT datname FROM pg_database;


\i 'J:/MaxKB/installer/init.sql'

tar -czvf maxkb_v1.10.1-lts.tar.gz C:\Users\a\Desktop\MaxKB


DROP DATABASE maxkb;








