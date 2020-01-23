import api
import requests.exceptions

def main():
    keyword = input('Keyword of title search: ')

    try:
        results = api.find_movie_by_title(keyword)

        print(f'There are {len(results)} movies found.')
        for r in results:
            print(f'{r.title} with code {r.imdb_code} has score {r.imdb_score}')
    except requests.exceptions.ConnectionError:
        print('Error: Could not find server. Check your network connection.')
    except ValueError:
        print('Error: You must specify a search term.')
    except Exception as ex:
        print(f"Oh that didn't work. {ex}")

if __name__ == '__main__':
    main()