import api


def main():
    results = api.find_movie_by_title('runner')

    print(f'There are {len(results)} movies found.')
    for r in results:
        print(f"Title: {r.get('title')}")


if __name__ == '__main__':
    main()
