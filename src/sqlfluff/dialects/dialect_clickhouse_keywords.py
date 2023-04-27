"""A list of ClickHouse keywords."""

UNRESERVED_KEYWORDS = [
    # All keywords are unreserved. They are only treated as reserved according to
    # context.
    # See: https://clickhouse.com/docs/en/sql-reference/syntax/#keywords
    # This means that, for example, using `join` or `select` as table identifiers
    # without quotes is allowed.
    "ADD",
    "AFTER",
    "ALIAS",
    "ALL",
    "ALTER",
    "AND",
    "ANTI",
    "ANY",
    "ARRAY",
    "AS",
    "ASCENDING",
    "ASOF",
    "AST",
    "ASYNC",
    "ATTACH",
    "BETWEEN",
    "BOTH",
    "BY",
    "CHECK",
    "CLEAR",
    "CLUSTER",
    "CODEC",
    "COLLATE",
    "COLUMN",
    "COMMENT",
    "CONSTRAINT",
    "CREATE",
    "CUBE",
    "DATABASE",
    "DATABASES",
    "DATE",
    "DAY",
    "DEDUPLICATE",
    "DEFAULT",
    "DELAY",
    "DELETE",
    "DESC",
    "DESCENDING",
    "DESCRIBE",
    "DETACH",
    "DICTIONARIES",
    "DICTIONARY",
    "DISK",
    "DISTINCT",
    "DISTRIBUTED",
    "DROP",
    "ELSE",
    "END",
    "ENGINE",
    "EPHEMERAL",
    "EVENTS",
    "EXISTS",
    "EXPLAIN",
    "EXPRESSION",
    "EXTRACT",
    "FETCHES",
    "FINAL",
    "FIRST",
    "FLUSH",
    "FOR",
    "FORMAT",
    "FREEZE",
    "FROM",
    "FUNCTION",
    "GLOBAL",
    "GRANULARITY",
    "GROUP",
    "HAVING",
    "HIERARCHICAL",
    "HOUR",
    "ID",
    "IF",
    "ILIKE",
    "IN",
    "INDEX",
    "INF",
    "INJECTIVE",
    "INSERT",
    "INTO",
    "IS",
    "IS_OBJECT_ID",
    "KEY",
    "KILL",
    "LAST",
    "LAYOUT",
    "LEADING",
    "LIFETIME",
    "LIKE",
    "LIMIT",
    "LIVE",
    "LOCAL",
    "LOGS",
    "MATERIALIZE",
    "MATERIALIZED",
    "MAX",
    "MERGES",
    "MIN",
    "MINUTE",
    "MODIFY",
    "MONTH",
    "MOVE",
    "MUTATION",
    "NAN_SQL",
    "NO",
    "NOT",
    "NULL_SQL",
    "NULLS",
    "OFFSET",
    "OPTIMIZE",
    "OR",
    "OUTFILE",
    "POPULATE",
    "PREWHERE",
    "PRIMARY",
    "PROFILE",
    "PROJECTION",
    "QUARTER",
    "QUOTA",
    "RANGE",
    "RELOAD",
    "REMOVE",
    "RENAME",
    "REPLACE",
    "REPLICA",
    "REPLICATED",
    "ROLLUP",
    "SAMPLE",
    "SECOND",
    "SEMI",
    "SENDS",
    "SETTINGS",
    "SHOW",
    "SOURCE",
    "START",
    "STOP",
    "SUBSTRING",
    "SYNC",
    "SYNTAX",
    "SYSTEM",
    "TABLE",
    "TABLES",
    "TEMPORARY",
    "TEST",
    "THEN",
    "TIES",
    "TIMEOUT",
    "TIMESTAMP",
    "TO",
    "TOP",
    "TOTALS",
    "TRAILING",
    "TRIM",
    "TRUNCATE",
    "TTL",
    "TYPE",
    "UPDATE",
    "USE",
    "UUID",
    "VALUES",
    "VIEW",
    "VOLUME",
    "WATCH",
    "WEEK",
    "WHEN",
    "WHERE",
    "WITH",
    "YEAR",
]
