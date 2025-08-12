using Npgsql;
using System.Windows.Forms;


namespace discount_calculator;
public class dcc
{

    public Label dc(int calcul)
    {

        Label sum = new Label();



        if (calcul < 10000)
        {
            sum.Text = "0%";
            return sum;

        }
        else if (calcul > 300000)
        {
            sum.Text = "15%";
            return sum;

        }
        else if (calcul > 10000&& calcul < 50000)
        {
            sum.Text = "5%";
            return sum;

        }
        else if (calcul > 50000&& calcul < 300000)
        {
            sum.Text = "10%";
            return sum;

        }
        else
        {
            return sum;
        }

    }
}