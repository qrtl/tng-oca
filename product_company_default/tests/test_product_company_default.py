from odoo.tests.common import TransactionCase


class TestProductCompanyDefault(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product = cls.env["product.product"].create(
            {"name": "Test Product", "default_code": "Test"}
        )

    def test_product_company(self):
        # Check company of product (odoo standard behavior is false)
        self.assertEqual(self.product.company_id, self.env.company)
