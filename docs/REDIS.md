# Shared-state extension

The default cache and quota are process local. A Redis adapter must use atomic quota operations, tenant-scoped keys, bounded TTLs and failover semantics. No Redis adapter is claimed here.
