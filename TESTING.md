# Testing documentation

[Manual Testing](#manual-testing)

[Automated Testing](#automated-testing)

- [Django Unit Tests](#django-unit-tests)
- [HTML Validation Tests](#html-validation-tests)
- [CSS Validation Tests](#css-validation-tests)
- [Javascript Validation Tests](#javascript-validation-tests)
- [Python Validation Tests](#python-validation-tests)
- [Lighthouse Scores](#lighthouse-scores)
- [Browser Compatibility](#browser-compatibility)
- [Accessibility](#Accessibility)
- [Responsiveness](#Responsiveness)

## Manual Testing

| #   | User Story                                        | Test Steps                                                | Expected Result                                 | Pass/Fail |
| --- | ------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------- | --------- |
| 1   | As an admin I can manage users' accounts          | Login as admin → Go to User Management → Edit/Delete user | Admin can view, edit, and delete user accounts  | Pass      |
| 2   | As an admin I can manage products                 | Login → Go to Products → Add/Edit/Delete product          | Product is added, updated, or deleted correctly | Pass      |
| 3   | As an admin I can view created orders             | Login → Go to Orders → View details → Amend               | Orders are viewable and editable                | Pass      |
| 4   | As an admin I can delete any comments             | Login → Go to Comments → Delete selected                  | Comment is removed from site                    | Pass      |
| 5   | As an admin I can view messages from contact form | Login → Go to Contact Messages → Read messages            | Messages are visible and complete               | Pass      |
| 6   | As a user I can create or edit my account         | Go to Register → Fill form → Submit → Edit profile        | Account is created and editable                 | Pass      |
| 7   | As a user I can login                             | Go to Login → Enter credentials → Submit                  | User is logged in and redirected                | Pass      |
| 8   | As a user I can search for products               | Enter search term → Click search                          | Relevant results are shown                      | Pass      |
| 9   | As a user I can sort products by criteria         | Use sort dropdown → Choose price/category                 | Product list is reordered correctly             | Pass      |
| 10  | As a user I can browse through products           | Go to Products page → Scroll and explore                  | Products are viewable and paginated             | Pass      |
| 11  | As a user I can view product details              | Click on a product                                        | Product page shows full details                 | Pass      |
| 12  | As a user I can add products to cart              | Click “Add to Cart” on a product                          | Item appears in cart                            | Pass      |
| 13  | As a user I can view cart contents                | Click Cart icon or link                                   | Cart contents are shown                         | Pass      |
| 14  | As a user I can update cart                       | Change quantity or remove item → Save                     | Cart updates correctly                          | Pass      |
| 15  | As a user I can view order summary                | Go to Checkout → Review items & total                     | Accurate order summary displayed                | Pass      |
| 16  | As a user I can checkout securely                 | Proceed to payment → Enter details → Submit               | Payment is processed securely                   | Pass      |
| 17  | As a user I can view all reviews                  | Go to product page → Scroll to reviews                    | Reviews are visible                             | Pass      |
| 18  | As a user I can add a review                      | Go to product → Click “Add Review” → Submit               | Review appears after submission                 | Pass      |
| 19  | As a user I can use contact form                  | Go to Contact page → Fill form → Submit                   | Confirmation message shown                      | Pass      |
| 20  | As a user I can sign up to newsletter             | Enter email in newsletter box → Submit                    | Success confirmation displayed                  | Pass      |

### Manual Testing Demo

![Demo](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749732537/curlculture_ovlbjd.gif)

## Automated Testing

## HTML Validation Tests

- **HTML Validation**: Used the [W3C HTML Validator](https://validator.w3.org/) which returned the following results:

![HTML Validation](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741776880/html_whfkh0.png)

## CSS Validation Tests

- **CSS Validation**: Used the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) which returned the following results:

![CSS Validation](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741776868/css_qumr2s.png)

## Javascript Validation Tests

- **JavaScript Validation**: Used [JSHint](https://jshint.com/) to validate JavaScript code

![calendar.js](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741719302/jshint_cragmi.png)

## Python Validation Tests

- **Python Validation**: Used [CI Python Linter](https://pep8ci.herokuapp.com/) to validate Python code. My website comprises of 7 apps with an average of 4 python files each. I have tested all of them but attaching all the screenshots will overcrowd this document. I have cleaned them up according to the pep8 report. There are few others that shortning the character length would beat pep8 purpose of readability as they were only one character over the limit and sometimes it would just be a closing bracket.

![Passed Validation](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741778048/errror_none_d2vo8p.png)

![Validation Fail](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741778048/error_yes_d8uakr.png)

## Lighthouse Scores

- **Lighthouse Scores**: Used [Lighthouse Metrics](https://lighthouse-metrics.com/) to measure the scores

### Scores for Home Page

![Home](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741779211/lighthouse_home_wqsuy4.png)

### Scores for Dashboard

![Dashboard](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741779210/lighthouse_dashboard_osmhbz.png)

## Browser Compatibility

The website was manually tested in chrome, firefox and edge and it worked accross those different browsers

## Accessibility

- **Accessibility**: Used [WAVE](https://wave.webaim.org/). I could only manage to test the pages that are accessible without login, for the other pages, I used the report I got from home page to clean them up.

![Accessibility](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741775364/wave_home_lejwi3.png)

![Accessibility](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741775365/wave_login_xygasm.png)

![Accessibility](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741775365/wave_signup_glpfbf.png)

## Responsiveness

- **Responsiveness**: Used [Am I responsive](https://ui.dev/amiresponsive). I had to download Ignore X-frames extesion to be able to use the test. However, I could only manage to test the home page and login page as there was a security warning when I logged in.

![Responsiveness](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741716797/responsive_home_qv2vst.png)

![Responsiveness](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741716797/responsive_login_fdmh3o.png)

![Responsiveness](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741716797/responsive_error_iur23j.png)
