import repository.posts.postsRepo as postsRepo
import repository.posts.mockPostRepo as mockPostRepo
import repository.rss.rssRepo as rssRepo
import repository.posts.mongoRepo as mongoRepo
import schema

if __name__ == "__main__":

    posts_repo: postsRepo.PostsRepository = mongoRepo.MongoPostsRepository()

    #posts_repo.update_post_score("f82e6a3b227d5a4d370dd8c9ff13301bc9811ef69e58a22c5388f6627b219f60", 1)
    #exit()

    #posts = posts_repo.get_all_posts()
    #print(posts)
    #exit()

    post = schema.Post(title="Bad news", description="Very bad news happened :(", source="badnews.com", link="badnews.com/badnews")
    posts_repo.insert_post(post)
    exit()

    response = posts_repo.get_post_by_hash("f82e6a3b227d5a4d370dd8c9ff13301bc9811ef69e58a22c5388f6627b219f60")

    print(response.__dict__)

    exit()

    urls = ["https://www.lrt.lt/?rss", "https://www.15min.lt/rss"]

    posts_repo: postsRepo.PostsRepository = mockPostRepo.MockPostsRepository()
    rss_repo: rssRepo.RssRepo = rssRepo.RssRepoImpl()

    posts = rss_repo.get_posts_from_urls(urls)

    for post in posts:
        print(post.title)
        print(post.link)

