from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from random import choice

comment = ['Love this vibe!', 'This is everything!',
           'So much creativity in one post!', 'Your feed is a masterpiece.',
           "You're killing it!", "Can't get enough of your content.", 'Always raising the bar!',
           "You're a true talent.", 'Your posts brighten my day.', 'Keep shining bright!', 'Amazing content as always.',
           'This is pure gold!', 'So much inspiration here.', 'Your posts never disappoint.',
           'Keep doing what you love!', 'Your passion shines through.', 'Wow, just wow!', "You're unstoppable!",
           'Never stop creating.', 'Loving every bit of this!', 'Your creativity knows no bounds.',
           'Your posts always make me smile.', 'Keep spreading positivity!', 'Absolutely mesmerizing.',
           'This is so impressive!', 'Your hard work is paying off.', 'So proud of you!',
           "Can't stop admiring your feed.", 'Your dedication is inspiring.',
           "You're a true gem.", 'Your posts speak to my soul.', 'Always leaving me in awe.',
           'Your authenticity is refreshing.', 'Keep shining your light!', "You're making a difference.",
           'So much love for this!', 'Your energy is contagious.', 'Always on point!', "Can't wait to see more.",
           'This is epic!', 'Your posts are a breath of fresh air.', 'Absolutely loving this vibe.',
           'Your creativity is unmatched.', 'Keep being awesome!', 'This is why I love following you.',
           'Your perspective is unique.', 'Your posts are a work of art.', 'So much talent in one place.',
           "You're an inspiration to many.", 'Always leaving me inspired.', 'Your posts always brighten my day.',
           'Keep slaying!', 'This is what perfection looks like.', "Can't get enough of your feed.",
           'Your creativity is on another level.', 'So much love for this content!', "You're setting the bar high!",
           'Your posts are a mood.', 'Absolutely captivating!', 'Keep blessing our feeds!', 'Your content speaks volumes.',
           'Your passion shines through every post.', 'This is beyond amazing!', "You're a true talent.",
           'Always leaving me speechless.', 'Your posts are a masterpiece.', 'Your energy is contagious!',
           'This deserves all the love!', 'So much talent in one feed.', 'Your posts are fire!', "You're slaying the game!",
           'This is legendary!', "Can't stop admiring your content.", 'Your posts are a work of art.', 'So much creativity in one place.',
           'Absolutely iconic!', 'Your feed is goals.', 'Keep inspiring us!', 'Your content is top-notch.', "You're a true influencer.",
           'So much respect for your hustle.', 'Your posts are a breath of fresh air.', "You're on a whole other level!",
           'This is why I love following you.', 'Your authenticity shines through.', 'Your posts are so relatable.',
           'Keep being amazing!', 'This is everything I needed to see.', 'Your posts always make my day better.',
           'Your content is always on point.', "You're a true trendsetter.", 'So much love for your creativity.',
           "Can't help but double-tap every post!", 'Your posts are pure gold.', 'Keep being unapologetically yourself!',
           'Your feed is a constant inspiration.', 'Your content is always a highlight.', "You're making waves!",
           'Your creativity is boundless.', 'Keep shining bright like you always do!', 'Your posts are a daily dose of inspiration!',
           'Your creativity is out of this world.', "Can't help but smile when I see your content.", 'Your feed is like a ray of sunshine.', 'Your posts always make my day brighter.', 'This is the content I live for!', "You're a true innovator.", 'Your posts are a vibe.', 'Your talent knows no bounds.', 'Keep blessing our feeds with your awesomeness!', 'So much love for your unique perspective.', 'Your content always stands out.', "You're a breath of fresh air on my feed.", 'Your posts make the world a better place.', 'Your passion shines through every post.', "You're a true gem in the Instagram community.", 'Your posts never fail to impress.', "Can't get enough of your amazing content.", 'Your creativity is unmatched!', 'Keep shining like the star you are.', 'Your posts are like a work of art.', 'Your captions are always on point!', 'Your authenticity is truly refreshing.', "You're a true original.", 'Your feed is a masterpiece in the making.', 'So much talent, so much love for your content!', 'Your posts brighten up even the gloomiest days.', "Keep doing what you're doing because you're doing it right!", 'Your content is always a highlight of my day.', 'Your posts deserve all the love and more.', "You're an absolute legend!", 'Your posts speak volumes without saying a word.', 'Your creativity is simply mind-blowing.', "You're a force to be reckoned with.", 'Your feed is like a treasure trove of inspiration.', 'Your posts make scrolling through Instagram worthwhile.', "You're the reason why I love Instagram!", 'Your content resonates with so many people.', 'Keep being the amazing human being that you are.', 'Your posts are the epitome of perfection.', 'Your creativity is on fire!', "Can't stop admiring your incredible talent.", 'Your posts leave a lasting impression.', 'Your passion is palpable in every post.', "You're an absolute rockstar!", 'Your posts are like a breath of fresh air.', 'Your content is a true masterpiece.', "You're destined for greatness.", 'Your posts make the world a brighter place.', 'Your creativity knows no limits!', 'Your posts always leave me inspired.', "You're a true trailblazer.", 'Your content is pure magic.', "Can't help but be in awe of your talent.", 'Your posts are like a burst of positivity.', 'Your creativity is contagious!', "You're a breath of fresh air on my timeline.", 'Your posts are always a delightful surprise.', 'Keep shining your light for the world to see.', 'Your posts make my day 100 times better!', "You're a true visionary.", 'Your content is a constant source of joy.', "Can't stop scrolling through your amazing feed.", 'Your passion shines through in everything you do.', 'Your posts are a testament to your brilliance.', "Keep doing what you love, you're killing it!", 'Your content is a ray of sunshine on my feed.', "You're making waves with your creativity.", 'Your posts are a masterclass in content creation.', "Keep being unapologetically yourself, it's beautiful.", 'Your feed is like a daily dose of happiness.', 'Your creativity is truly inspiring.', "You're a true gem in the Instagram community.", 'Your posts never fail to put a smile on my face.', 'Your content is like a work of art.', 'Keep being the amazing soul that you are.', 'Your posts have a way of brightening up my day.', "You're a true icon!", 'Your creativity is on another level.', 'Your posts deserve all the love and more.', "You're a force to be reckoned with.", 'Your content speaks to my heart.', 'Keep slaying the game!', 'Your posts are simply breathtaking.', "You're a true inspiration to many.", 'Your creativity knows no bounds.', 'Your posts are like a ray of sunshine on a cloudy day.', 'Keep blessing my feed with your amazing content!', 'Your talent is undeniable.', 'Your posts are like a warm hug on the internet.', "You're a true original.", 'Your content is like a burst of energy.', 'Your posts make me believe in magic.', 'Keep shining bright like the star you are.', 'Your creativity is what makes Instagram so special.', 'Your posts are like a breath of fresh air.', "You're a beacon of light in the online world.", 'Your content always leaves me wanting more.', 'Keep being the amazing human being that you are.', 'Your posts make the world a better place.', 'Your posts always bring joy to my feed.', "You're a true inspiration!", 'Your content is a masterpiece.', "Can't get enough of your amazing feed!", 'Your creativity lights up my screen.', "You're the reason why I love Instagram!", 'Your posts are like a dose of happiness.', "Keep shining bright, you're a star!", 'Your talent shines through in every post.', 'Your content is like a ray of sunshine.', 'Your posts are always on point!', "You're a true trendsetter.", 'Your creativity is truly admirable.', 'Your posts are a work of art.', "Keep doing what you're doing because you're nailing it!", 'Your feed is goals!', 'Your content is a breath of fresh air.', "You're a true gem in the Instagram community.", 'Your posts always make my day.', "Can't help but double-tap every single post!", 'Your creativity is unmatched.', 'Your posts deserve all the love and appreciation.', 'Keep blessing our feeds with your awesomeness!', 'Your content is like a ray of sunshine on a rainy day.', 'Your posts are like a warm hug on the internet.', "You're a true rockstar!", 'Your creativity knows no bounds.', 'Your posts are a constant source of inspiration.', 'Keep being the amazing soul that you are.', 'Your posts always leave me in awe.', 'Your content is like a breath of fresh air.', "You're a true visionary.", 'Your posts brighten up even the darkest days.', 'Your creativity is simply magical.', 'Keep being unapologetically yourself!', 'Your posts make scrolling through Instagram worthwhile.', "You're a true influencer.", 'Your content is top-notch.', 'Your posts make the world a better place.', "Can't stop admiring your incredible talent.", 'Your creativity is what makes Instagram so special.', 'Your posts are like a burst of positivity.', "You're a true icon in the making.", 'Your content always leaves me inspired.', 'Keep slaying the game!', 'Your posts are like a treasure trove of inspiration.', "You're a true legend!", 'Your creativity is contagious.', 'Your posts deserve all the recognition.', 'Keep being the amazing human being that you are.', 'Your posts are a ray of sunshine in my feed.', "You're a true source of inspiration.", 'Your content always brightens my day!', "Can't get enough of your amazing feed.", 'Your creativity shines through in every post.', 'Keep spreading your positivity!', 'Your posts are like a breath of fresh air.', 'Your passion for what you do is evident in every post.', "You're a true artist.", 'Your feed is like a daily dose of happiness.', 'Your content speaks to my soul.', "Keep doing what you're doing, you're rocking it!", 'Your posts always leave me feeling inspired.', 'Your creativity is unmatched!', "You're a true trendsetter.", 'Your posts make my day 100 times better.', 'Keep being the amazing person you are!', 'Your posts always brighten up my day.', "You're a constant source of inspiration.", 'Your content is always top-notch.', 'Your posts are like a warm hug on the internet.', 'Keep shining bright like the star you are!', 'Your creativity is simply mind-blowing.', 'Your posts deserve all the love!', "You're an absolute legend!", 'Your feed is goals.', "Keep doing you because you're amazing!", 'Your posts are a work of art.', 'Your content always puts a smile on my face.', "You're making a positive impact with your posts.", 'Your creativity is off the charts!', 'Your posts are a reflection of your beautiful soul.', 'Keep being the incredible human being that you are.', 'Your posts are like a burst of positivity.', "You're a true inspiration to many.", 'Your content makes me believe in magic.', "Keep shining, you're unstoppable!", 'Your posts are like a ray of sunshine.', 'Your creativity is contagious!', "You're a true role model.", 'Your content is like a breath of fresh air.', 'Keep blessing our feeds with your awesomeness.', 'Your posts always leave me in awe.', "You're a beacon of light in the online world.", 'Your creativity knows no bounds.', 'Your posts always leave a lasting impression.', "Keep being authentic, it's beautiful.", 'Your content is always on point.', "You're a true gem in the Instagram community.", 'Your posts are like a work of art.', 'Keep being the amazing person you are.', 'Your posts are pure magic!', 'Your creativity is what makes Instagram so special.', "You're a true original.", 'Your content always brightens my day!', 'Keep shining your light for the world to see.', 'Your posts are like a breath of fresh air.', 'Your passion for what you do is truly inspiring.', "You're a constant source of inspiration.", 'Your creativity shines through in every post.', 'Keep spreading your positivity!', 'Your posts always leave me feeling inspired.']
def likecomment(username, password,hashtag,number_of_post=3, retry=5):
    liked = 0
    # Configuration
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.41")

    for _ in range(retry):
        driver = webdriver.Edge(options=options)
        try:
            driver.get("https://www.instagram.com/")
            time.sleep(2)
        except:
            print("Can't reach Website!!!")
            driver.quit()
            continue

        # Login
        try:
            driver.find_element(By.XPATH, '''//*[@id="loginForm"]/div/div[1]/div/label/input''').send_keys(username)
            driver.find_element(By.XPATH, '''//*[@id="loginForm"]/div/div[2]/div/label/input''').send_keys(password)
            driver.find_element(By.XPATH, '''//*[@id="loginForm"]/div/div[3]''').click()
            time.sleep(8)
        except:
            print("Login Failed")
            driver.quit()
            continue

        try:
            driver.find_element(By.XPATH,'''/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div/div[1]/div/div''').click()
            driver.find_element(By.XPATH,'''/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input''').send_keys(hashtag)
            time.sleep(2)
            driver.find_element(By.XPATH,'''/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]/div/div''').click()
            time.sleep(5)
            driver.find_element(By.XPATH,'''/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/article/div/div/div/div[1]/div[1]/a''').click()
            time.sleep(2)
            for _ in range(number_of_post):
                driver.find_element(By.CSS_SELECTOR,'''svg[aria-label="Like"]''').click()
                time.sleep(1)
                driver.find_element(By.CSS_SELECTOR, 'textarea[aria-label="Add a comment…"]').click()
                time.sleep(1)
                actions = ActionChains(driver)
                actions.send_keys(choice(comment))
                actions.send_keys(Keys.RETURN)
                actions.send_keys(Keys.ARROW_RIGHT)
                actions.perform()
                time.sleep(2)
                liked +=1


            print("Number of Posts Liked and Commented:",liked)
            driver.quit()
            break
        except Exception as error :
            print(error)
            print("Process failed")
            print("Number of Posts Liked and Commented:", liked)
        driver.quit()


# likecomment("everydaynewscommunity", "n1e2w3s4", "#snake")
