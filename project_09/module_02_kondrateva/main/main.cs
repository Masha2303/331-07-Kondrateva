using Npgsql;
using database;
using discount_calculator;
namespace main
{
    public partial class main : Form
    {
        private string connect = "host = localhost; username = postgres; database = postgres; password = KUR03102005kur;";

        public main()
        {
            InitializeComponent();
            metod1();
        }
        public Label Metod2(string name)
        {
            int calcul = 0;
            Label sum = new Label();
            MyClass obj = new MyClass();
            dcc dc = new dcc();
            NpgsqlDataReader reader = obj.db($"select ammount from partner_products_import where name_partners in ('{name}')");
            NpgsqlConnection connection = new NpgsqlConnection(connect);
            connection.Open();
          
            while (reader.Read())
            {
                calcul += reader.GetInt32(0);
            }
            sum = dc.dc(calcul);
            sum.AutoSize = true;
            sum.Location = new Point(200, 50);
            return sum;

        }
        public void metod1()
        {
            {
                NpgsqlConnection connection = new NpgsqlConnection(connect);
                connection.Open();
                NpgsqlCommand command = new NpgsqlCommand("select*from partners_import", connection);
                NpgsqlDataReader reader = command.ExecuteReader();
                int y = 0;
                while (reader.Read())
                {
                    Panel panel = new Panel();
                    {
                        panel.Size = new Size(400, 100);
                        panel.BorderStyle = BorderStyle.FixedSingle;
                        panel.Location = new Point(5, y);
                    }

                    Label type_name = new Label();
                    {
                        type_name.Text = $"{reader.GetString(0)} | {reader.GetString(1)}";
                        type_name.AutoSize = true;
                        type_name.Location = new Point(0, 0);
                    }
                    Label director = new Label();
                    {
                        director.Text = $"{reader.GetString(2)} ";
                        director.AutoSize = true;
                        director.Location = new Point(0, 15);
                    }
                    Label telephone_number = new Label();
                    {
                        telephone_number.Text = $"+7 {reader.GetString(4)} ";
                        telephone_number.AutoSize = true;
                        telephone_number.Location = new Point(0, 35);
                    }
                    Label reiting = new Label();
                    {
                        reiting.Text = $"Рейтинг: {reader[7]} ";
                        reiting.AutoSize = true;
                        reiting.Location = new Point(0, 55);
                    }

                    y = y + 130;
                    Label sum = Metod2(reader.GetString(1));
                    this.Controls.Add(panel);
                    panel.Controls.Add(sum);
                    panel.Controls.Add(type_name);
                    panel.Controls.Add(director);
                    panel.Controls.Add(telephone_number);
                    panel.Controls.Add(reiting);

                }
            }
        }
    }
}
