<template>
  <footer>
    <div class="container-fluid">
      <div class="row">
        <!-- Quick Links start -->
        <div class="col-lg-4 col-md-4">
          <h3>Quick Links</h3>
          <ul class="list-unstyled">
            <li>
              <a href="/" style="color: #fff;">Home Page</a>
            </li>
            <li>
              <a href="#" style="color: #fff;">Back to top</a>
            </li>
          </ul>
        </div>
        <!-- Quick Links end -->

        <!-- Thanks to start -->
        <div class="col-lg-4 col-md-4">
          <h3>Thanks to</h3>
          <ul class="list-unstyled">
            <li>
              <a href="https://google.com" style="color: #fff;">Google</a>
            </li>
            <li>
              <a href="https://getbootstrap.com/" style="color: #fff;">Bootstrap</a>
            </li>
          </ul>
        </div>
        <!-- Thanks to end -->

        <!-- Contact us start -->
        <div class="col-lg-4 col-md-4">
          <h3>Contact us</h3>
          <ul class="list-unstyled">
            <li>TEL: +61 123456</li>
            <li>Email: unsw@mail.com</li>
          </ul>
        </div>
        <!-- Contact us end -->
      </div>

      <!-- social icons start -->
      <a href="https://facebook.com" style="color: #fff;">
        <i class="social-icon fab fa-facebook-f"></i>
      </a>
      <a href="https://twitter.com" style="color: #fff;">
        <i class="social-icon fab fa-twitter"></i>
      </a>
      <a href="https://instagram.com" style="color: #fff;">
        <i class="social-icon fab fa-instagram"></i>
      </a>
      <a href="https://www.unsw.edu.au/" style="color: #fff;">
        <i class="social-icon fas fa-envelope"></i>
      </a>
      <!-- social icons end -->

      <p>© All right Reversed. 9323 Group 14.</p>
    </div>
  </footer>
</template>

<script>
export default {
  name: "Footer"
};
</script>

<style scoped>
footer {
  padding-top: 2rem;
  padding-bottom: 2rem;
  background-color: #69beaf;
  color: white;
}
.social-icon {
  margin: 30px 20px;
}
</style> 