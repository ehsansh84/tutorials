<!-- Space: RD -->
<!-- Title: What is Object Storage -->

### Defenition:
- A low performance storage at a low cost
- Each file is an object which has 4 specs:
  - A unique ID
  - Data
  - Metadata
  - Attributes (Related to permissions)
### Bucket
- A bucket can contain billions of object
- We can communicate buckets through APIs
- A bucket can store objects on multiple physical storage
- Buckets can be replicated in different zones

### Comparison:
- Object storage takes each piece of data and designates it as an object. Data is kept in separate storehouses versus files in folders and is bundled with associated metadata and a unique identifier to form a storage pool.
- File storage stores data as a single piece of information in a folder to help organize it among other data. This is also called hierarchical storage, imitating the way that paper files are stored. When you need access to data, your computer system needs to know the path to find it.
- Block storage takes a file apart into singular blocks of data and then stores these blocks as separate pieces of data. Each piece of data has a different address, so they don't need to be stored in a file structure.

### Benefits of object storage
Greater data analytics. Object storage is driven by metadata, and with this level of classification for every piece of data, the opportunity for analysis is far greater.
Infinite scalability. Keep adding data, forever. There's no limit.
Faster data retrieval. Due to the categorization structure of object storage, and the lack of folder hierarchy, you can retrieve your data much faster.
Reduction in cost. Due to the scale-out nature of object storage, it's less costly to store all your data.
Optimization of resources. Because object storage does not have a filing hierarchy, and the metadata is completely customizable, there are far fewer limitations than with file or block storage.


#### Refrences:
- [What is Object Storage?](https://www.youtube.com/watch?v=ZfTOQJlLsAs)
