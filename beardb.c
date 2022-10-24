
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdbool.h>

#define MAX_SIZE 100

typedef struct {
    char project[MAX_SIZE];
    char database[MAX_SIZE];
    bool database_active;
} Beardb;

typedef struct {
    char bucket_name[MAX_SIZE];
    bool database_active;
} Bucket;

Beardb* beardb_init(char* project)
{
    Beardb* beardb = malloc(sizeof(Beardb));
    strcpy(beardb->project, project);
    beardb->database_active = false;
    return beardb;
}

void beardb_load_database(Beardb* beardb, char* database)
{
    strcpy(beardb->database, database);
    beardb->database_active = true;
}

Bucket* bucket_init(Beardb* beardb, char* bucket_name)
{
    Bucket* bucket = malloc(sizeof(Bucket));
    strcpy(bucket->bucket_name, bucket_name);
    bucket->database_active = beardb->database_active;
    return bucket;
}

void bucket_insert(Bucket* bucket, char* data)
{
    if (!bucket->database_active) {
        printf("Error: No database loaded\n");
        return;
    }
    
    if (strlen(bucket->bucket_name) == 0) {
        printf("Error: Bucket name required\n");
        return;
    }
    
    // TODO: Implement
}

void bucket_update(Bucket* bucket, char* query, char* data)
{
    if (!bucket->database_active) {
        printf("Error: No database loaded\n");
        return;
    }
    
    if (strlen(bucket->bucket_name) == 0) {
        printf("Error: Bucket name required\n");
        return;
    }
    
    // TODO: Implement
}

void bucket_delete(Bucket* bucket, char* query)
{
    if (!bucket->database_active) {
        printf("Error: No database loaded\n");
        return;
    }
    
    if (strlen(bucket->bucket_name) == 0) {
        printf("Error: Bucket name required\n");
        return;
    }
    
    // TODO: Implement
}

char* bucket_fetch(Bucket* bucket, char* query)
{
    if (!bucket->database_active) {
        printf("Error: No database loaded\n");
        return NULL;
    }
    
    if (strlen(bucket->bucket_name) == 0) {
        printf("Error: Bucket name required\n");
        return NULL;
    }
    
    // TODO: Implement
    return NULL;
}

int main()
{
    Beardb* beardb = beardb_init("db");
    beardb_load_database(beardb, "users");
    
    Bucket* bucket = bucket_init(beardb, "users");
    bucket_insert(bucket, "id=1,name=John,age=21");
    bucket_insert(bucket, "id=2,name=Smith,age=32");
    bucket_insert(bucket, "id=3,name=Jane,age=27");
    
    printf("%s\n", bucket_fetch(bucket, "id=1"));
    printf("%s\n", bucket_fetch(bucket, "id=2"));
    printf("%s\n", bucket_fetch(bucket, "id=3"));
    
    bucket_update(bucket, "id=2", "id=2,name=Smith,age=33");
    printf("%s\n", bucket_fetch(bucket, "id=2"));
    
    bucket_delete(bucket, "id=3");
    printf("%s\n", bucket_fetch(bucket, "id=3"));
    
   
} 