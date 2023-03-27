
def seo_score(page):

    seo_score = 100

    if page.title_len > 70:
        seo_score -= 10
    elif page.title_len == 0:
        seo_score -= 20
    if page.title == 'Not Found':
        seo_score -= 30

    if page.response_time > 2:
        seo_score -= 20

    return seo_score
