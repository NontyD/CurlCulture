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

![HTML Validation](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749767953/html_gjlo12.png)

## CSS Validation Tests

- **CSS Validation**: Used the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) which returned the following results:

![CSS Validation](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749767946/css_i4wcn6.png)

**One error** is reported from the Font Awesome CDN stylesheet:
.fa-rotate-by { transform: rotate(var(--fa-rotate-angle, none)); }
var(--fa-rotate-angle, none) is not a transform value : rotate(var(--fa-rotate-angle, none))
This is a known issue with Font Awesome and does not affect the appearance or functionality of the site.
**Warnings about CSS variables:**
"Due to their dynamic nature, CSS variables are currently not statically checked". These warnings are informational and do not indicate errors in the CSS. The site uses CSS variables for flexibility and maintainability.
Conclusion:
All validation errors and warnings are either from trusted third-party libraries or are expected due to the use of CSS variables.
They do not impact the user experience or site functionality.

## Python Validation Tests

- **Python Validation**: All Python files were validated using [CI Python Linter](https://pep8ci.herokuapp.com/) for PEP8 compliance. The project consists of 6 Django apps, each with multiple Python files.
  - **Most files passed** the linter with no issues after cleanup.
  - In a few cases, some lines slightly exceeded the 79-character limit (usually by 1–2 characters, often for closing brackets or improved readability). These were left as-is to maintain code clarity and avoid unnecessary line breaks.
  - No critical PEP8 errors remain, and all warnings have been reviewed and addressed where possible.

![Passed Validation](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749787549/pass_py1yes.png)

![Validation Fail](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749787561/fail_hqs9ui.png)

## Lighthouse Scores

- **Lighthouse Scores**: Used [Lighthouse Metrics](https://lighthouse-metrics.com/) to measure the scores

### Scores for Home Page

![Home](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749767953/lighthouse_ui3mfc.png)

## Browser Compatibility

The website was manually tested in chrome, firefox and edge and it worked accross those different browsers

## Accessibility

- **Accessibility**: Used [WAVE](https://wave.webaim.org/). I could only manage to test the pages that are accessible without login, for the other pages, I used the report I got from home page to clean them up.

![Accessibility](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749769001/wave_hfgy5g.png)

## Responsiveness

- **Responsiveness**: Used [Am I responsive](https://ui.dev/amiresponsive). I had to download Ignore X-frames extesion to be able to use the test. However, I could only manage to test the home page and login page as there was a security warning when I logged in.

![Responsiveness](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749772821/responsive_uadmuc.png)
